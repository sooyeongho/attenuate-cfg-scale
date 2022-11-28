version 1.5 (2022.11.29)

This script attenuates the CFG Scale value while the image is being generated,
hopefully resulting in a smoother image. Experiment and enjoy!

Installation:

Copy attenuate-cfg-scale.py to webui/scripts folder (see https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts)

( Also check out: https://github.com/guzuligo/CFG-Schedule-for-Automatic1111-SD )


Examples:

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
