# Attenuate CFG Scale script for AUTOMATIC1111/stable-diffusion-webui
#
# https://github.com/tkalayci71/attenuate-cfg-scale
# version 1.0 - 2022.11.11

import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

class Script(scripts.Script):

    def title(self):
        return "Attenuate CFG Scale"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        strength = gr.Slider(value=1.00, label="Strength", minimum=0.00, maximum=1.00,   step=0.01)
        range_check = gr.Checkbox(label='Do not allow negative values', value=False)
        return [strength, range_check]

    def run(self, p, strength, range_check):
        target_value = p.cfg_scale * (1-strength)
        p.cfg_scale = Fake_float(p.cfg_scale, target_value, p.steps  * p.batch_size, range_check)
        proc = process_images(p)
        return proc

class Fake_float(float):
    def __new__(self, value, target, maxstep, range_check):
        return float.__new__(self, value)

    def __init__(self, value, target, maxstep, range_check):
        float.__init__(value)
        self.orig = value
        self.target = target
        self.maxstep = maxstep-1
        if (self.maxstep<1): self.maxstep=1
        self.range_check = range_check
        self.curstep = 0

    def __mul__(self,other):
        return self.fake_mul(other)

    def __rmul__(self,other):
        return self.fake_mul(other)

    def fake_mul(self,other):
        fake_value = self.orig - ( (self.orig-self.target) * (self.curstep/self.maxstep) )
        self.curstep += 1
        if (self.range_check==True):
            if (self.curstep > self.maxstep): self.curstep = self.maxstep
        return fake_value * other
