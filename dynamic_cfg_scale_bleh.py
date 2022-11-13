# Dynamic CFG Scale script for AUTOMATIC1111/stable-diffusion-webui
#
# https://github.com/tkalayci71/dynamic-cfg-scale
# version 1.2 - 2022.11.13

import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state
from math import floor, sin, cos, sqrt, pi
import io
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

misc_funcs = {'linear':lambda x : x,
            'square':lambda x : x*x,
            'root':lambda x : sqrt(x),
            'cos_1':lambda x: 1-((1+cos(x*pi))/2),
            'sin_1':lambda x: 1-((1+sin(x*pi))/2),
            'cos_2':lambda x: ((1+cos(x*pi*2))/2),
            'sin_2':lambda x: ((1+sin(x*pi*2))/2),
            'cos_3':lambda x: 1-((1+cos(x*pi*2))/2),
            'sin_3':lambda x: 1-((1+sin(x*pi*2))/2)
        }

class Script(scripts.Script):

    def title(self):
        return 'Dynamic CFG Scale'


    def show(self, is_img2img):
        return not(is_img2img)

    def ui(self, is_img2img):
        start_value = gr.Slider(label='Start', value=7, minimum=-30, maximum=+30, step=1)
        end_value = gr.Slider(label='End', value=0, minimum=-30, maximum=+30, step=1)
        func_names =[]
        for key in misc_funcs: func_names.append(key)
        interpolation_selector  = gr.Dropdown(label='Interpolation', choices=func_names, value=func_names[0])
        func_preview = gr.Image(value=get_func_preview(7,0,'linear'))

        interpolation_selector.change(fn=get_func_preview,inputs=[start_value, end_value, interpolation_selector],outputs=[func_preview])
        start_value.change(fn=get_func_preview,inputs=[start_value, end_value, interpolation_selector],outputs=[func_preview])
        end_value.change(fn=get_func_preview,inputs=[start_value, end_value, interpolation_selector],outputs=[func_preview])
        return [start_value, end_value, interpolation_selector]

    def run(self, p, start_value, end_value, interpolation_selector):

        if p.sampler_index in (0,1,2,7,8,10,14):
            max_mul_count = p.steps * p.batch_size
            steps_per_mul = p.batch_size
        elif p.sampler_index in (3,4,5,6,11,12,13):
            max_mul_count = ((p.steps*2)-1) * p.batch_size
            steps_per_mul = 2 * p.batch_size
        elif p.sampler_index==15: # ddim
            max_mul_count = fix_ddim_step_count(p.steps)
            steps_per_mul = 1
        elif p.sampler_index==16: # plms
            max_mul_count = fix_ddim_step_count(p.steps)+1
            steps_per_mul = 1
        else:
            return # 9=dpm adaptive

        saved_obj = p.cfg_scale
        p.cfg_scale = Fake_float(start_value, end_value, misc_funcs[interpolation_selector], max_mul_count, steps_per_mul)
        proc = process_images(p)
        if (p.cfg_scale.current_step!=0): print('!!!warning: unexpected value!!!')
        p.cfg_scale = saved_obj

        return proc

class Fake_float(float):
    def __new__(self, start_value, end_value, interpolation_func, max_mul_count, steps_per_mul):
        return float.__new__(self, start_value)

    def __init__(self, start_value, end_value, interpolation_func, max_mul_count, steps_per_mul):
        float.__init__(start_value)
        self.start_value = start_value
        self.end_value = end_value
        self.interpolation_func = interpolation_func
        self.max_mul_count = max_mul_count
        self.current_mul = 0
        self.steps_per_mul = steps_per_mul
        self.current_step = 0
        self.max_step_count = (max_mul_count // steps_per_mul) + (max_mul_count % steps_per_mul > 0)

    def __mul__(self,other):
        return self.fake_mul(other)

    def __rmul__(self,other):
        return self.fake_mul(other)

    def fake_mul(self,other):
        time = self.current_step/(self.max_step_count-1) #divbyzero?
        factor = self.interpolation_func(time)
        fake_value = self.start_value + (self.end_value - self.start_value)* factor
        self.current_mul = (self.current_mul+1) % self.max_mul_count
        self.current_step = (self.current_mul) // self.steps_per_mul
        return fake_value * other

def fix_ddim_step_count(steps):
    valid_step = 999 / (1000 // steps)
    if valid_step == floor(valid_step): steps=int(valid_step)+1
    if ((1000 % steps)!=0): steps +=1
    return steps

def get_func_preview(start_value, end_value, interpolation):
    max_step_count = 20
    interpolation_func = misc_funcs[interpolation]
    results = []
    steps = np.linspace(0,max_step_count)
    for current_step in steps:
        time = current_step/(max_step_count-1) #divbyzero?
        factor = interpolation_func(time)
        fake_value = start_value + (end_value - start_value)* factor
        results.append(fake_value)
    plt.figure()
    plt.plot(steps,results)
    img = fig2img(plt)
    return img

def fig2img(fig):
    buf = io.BytesIO()
    fig.savefig(buf,dpi=60)
    buf.seek(0)
    img = Image.open(buf)
    return img

