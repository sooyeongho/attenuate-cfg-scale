# Attenuate CFG Scale script for AUTOMATIC1111/stable-diffusion-webui
#
# https://github.com/tkalayci71/attenuate-cfg-scale
# version 1.5 - 2022.11.29
#
# also check out:
# https://github.com/guzuligo/CFG-Schedule-for-Automatic1111-SD

import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state
from math import floor

class Script(scripts.Script):

    def title(self):
        return "Attenuate CFG Scale"

    def show(self, is_img2img):
        return not(is_img2img)

    def ui(self, is_img2img):
        strength = gr.Slider(value=1.00, label="Strength", minimum=0.00, maximum=2.00, step=0.1)
        return [strength]

    def run(self, p, strength):

        if p.sampler_name in ('Euler a','Euler','LMS','DPM++ 2M','DPM fast','LMS Karras','DPM++ 2M Karras'):
            max_mul_count = p.steps * p.batch_size
            steps_per_mul = p.batch_size
        elif p.sampler_name in ('Heun','DPM2','DPM2 a','DPM++ 2S a','DPM2 Karras','DPM2 a Karras','DPM++ 2S a Karras','DPM++ SDE','DPM++ SDE Karras'):
            max_mul_count = ((p.steps*2)-1) * p.batch_size
            steps_per_mul = 2 * p.batch_size
        elif p.sampler_name=='DDIM':
            max_mul_count = fix_ddim_step_count(p.steps)
            steps_per_mul = 1
        elif p.sampler_name=='PLMS':
            max_mul_count = fix_ddim_step_count(p.steps)+1
            steps_per_mul = 1
        else:
            print('!!!warning: unsupported sampler ',p.sampler_name)
            return

        target_value = p.cfg_scale * (1-strength)
        saved_obj = p.cfg_scale
        p.cfg_scale = Fake_float(p.cfg_scale, target_value, max_mul_count, steps_per_mul)
        proc = process_images(p)
        if (p.cfg_scale.current_step!=0): print('!!!warning: unexpected value!!!')
        p.cfg_scale = saved_obj

        return proc

class Fake_float(float):
    def __new__(self, orig_value, target_value, max_mul_count, steps_per_mul):
        return float.__new__(self, orig_value)

    def __init__(self, orig_value, target_value, max_mul_count, steps_per_mul):
        float.__init__(orig_value)
        self.orig_value = orig_value
        self.target_value = target_value
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
        if (self.max_step_count==1):
            fake_value= self.orig_value
        else:
            fake_value = self.orig_value + (self.target_value - self.orig_value)*(self.current_step/(self.max_step_count-1))
        self.current_mul = (self.current_mul+1) % self.max_mul_count
        self.current_step = (self.current_mul) // self.steps_per_mul
        return fake_value * other

def fix_ddim_step_count(steps):
    valid_step = 999 / (1000 // steps)
    if valid_step == floor(valid_step): steps=int(valid_step)+1
    if ((1000 % steps)!=0): steps +=1
    return steps
