version 1.4 (2022.11.21)

This script attenuates the CFG Scale value while the image is being generated,
hopefully resulting in a smoother image. Experiment and enjoy!

Installation:

Copy attenuate-cfg-scale.py to webui/scripts folder (see https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts)

( Also check out: https://github.com/guzuligo/CFG-Schedule-for-Automatic1111-SD )


Examples:

(Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3294549032, Size: 512x512, Model hash: 7460a6fa)

Prompt:'einstein'
Before | After
--- | ---
![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00000-3294549032-einstein.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00001-3294549032-einstein.png)

Prompt:'mona lisa'
Before | After
--- | ---
![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00002-3294549032-mona%20lisa.png)|![image](https://github.com/tkalayci71/attenuate-cfg-scale/blob/main/examples/00003-3294549032-mona%20lisa.png)
