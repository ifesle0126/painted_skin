#!coding: utf-8

import base64
import requests

mask_config = {
    "model": "u2netp",
    "return_mask": True,
    "alpha_matting": True,
    "alpha_matting_foreground_threshold": 240,
    "alpha_matting_background_threshold": 10,
    "alpha_matting_erode_size": 10
}

def get_mask_img_base64(img_path):
    with open(img_path, 'rb') as f:
        img_data = f.read()
        init_img_base64 = base64.b64encode(img_data).decode("ascii")
    mask_config["input_image"] = init_img_base64
    response = requests.post(url = 'http://127.0.0.1:7860/rembg', json = mask_config, headers = {"Content-Type": "application/json"})
    print("get mask img status: ", response.status_code)
    return response.json()['image']

if __name__ == '__main__':
    mask_img_path = './img/mask.jpg'
    with open(mask_img_path, 'wb') as f:
        f.write(base64.b64decode(get_mask_img_base64("./img/111.jpg")))
