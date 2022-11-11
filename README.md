# attenuate-cfg-scale
Attenuate CFG Scale script for AUTOMATIC1111/stable-diffusion-webui

Usage:

Copy attenuate-cfg-scale.py to webui/scripts folder

see https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts

This script attenuates the CFG Scale value while the image is being generated,
hopefully resulting in a smoother image. Experiment and enjoy!

examples:

(Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3294549032, Size: 512x512, Model hash: 7460a6fa)

Prompt:'einstein'

![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00000-3294549032-einstein.png)

![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00001-3294549032-einstein.png)

Prompt:'mona lisa'

![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00002-3294549032-mona%20lisa.png)

![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00003-3294549032-mona%20lisa.png)


Parameters:

Strength: in the final step, CFG scale will have been multiplied by (1-strength)

Do not allow negative values: prevents CFG scale from going lower than zero, for some samplers (like HEUN) this is a known issue

Known issues:

Does not work well if batch count is greater than 1 and for samplers that do more than one multiplication per step.
