#! coding: utf-8

import requests
import calendar
import time
import get_mask_img
import img_upload
import sys
import base64
import datetime


batch_size = 2
inpaint_config = {
    # "init_images": [init_img_base64],
    # "mask": mask_img_base64,
    "mask_blur": 4,
    "inpainting_mask_invert": 1,
    "sampler_index": "DPM++ SDE Karras",
    "denoising_strength": 1,
    # "prompt": prompt,
    "batch_size": batch_size
}

def img2img(img_path, prompt):
    inpaint_config['mask'] = get_mask_img.get_mask_img_base64(img_path)
    inpaint_config['prompt'] = prompt
    with open(img_path, 'rb') as f:
        img_data = f.read()
        init_img_base64 = base64.b64encode(img_data).decode("ascii")
        inpaint_config['init_images'] = [init_img_base64]
    response = requests.post(url='http://127.0.0.1:7860/sdapi/v1/img2img', json=inpaint_config, headers={"Content-Type": "application/json"})
    print("get img2img status: ", response.status_code)
    inpaint_imgs = []
    for i in range(batch_size):
        new_img_name = "inpaint_img_" +  str(calendar.timegm(time.gmtime())) + ".png"
        rst_img_path = './img/' + new_img_name
        img_str = response.json()['images'][i];
        with open(rst_img_path, 'wb') as f:
            f.write(base64.b64decode(img_str))
        print(f"inpaint img. {rst_img_path}", datetime.datetime.now())
        inpaint_imgs[i] = rst_img_path
    return inpaint_imgs

if __name__ == "__main__":
    print(img2img(sys.argv[1], sys.argv[2]))

