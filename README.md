# version 1.5 (2022.11.29)

This script attenuates the CFG Scale value while the image is being generated,
hopefully resulting in a smoother image. Experiment and enjoy!

(Also check out: https://github.com/guzuligo/CFG-Schedule-for-Automatic1111-SD)

# Installation:

Copy ![attenuate-cfg-scale.py](https://raw.githubusercontent.com/tkalayci71/attenuate-cfg-scale/main/attenuate_cfg_scale.py) to webui/scripts folder (see https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts)

(if you're updating from an earlier version and strength parameter does not go to 2, edit/remove lines containing "attenuate_cfg_scale.py" in ui-config.json)

# Usage:

In txt2img tab, select "Attenuate CFG scale" in the "Script" list at the bottom, set strength parameter, and click Generate button.


# Examples:

(Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3294549032, Size: 512x512, Model hash: 7460a6fa sd-v1-4.ckpt)

Prompt:'einstein'
Before (strength=0) | After (strength=1) | After (strength=2) 
--- | --- | ---
![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00000-3294549032-einstein.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00001-3294549032-einstein.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00004-3294549032-einstein.png)

Prompt:'mona lisa'
Before (strength=0) | After (strength=1) | After (strength=2) 
--- | --- | ---
![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00002-3294549032-mona%20lisa.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00003-3294549032-mona%20lisa.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00005-3294549032-mona%20lisa.png)

Prompt:'elvis'
Before (strength=0) | After (strength=1) | After (strength=2) 
--- | --- | ---
![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00000-3294549032-elvis.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00001-3294549032-elvis.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00002-3294549032-elvis.png)
