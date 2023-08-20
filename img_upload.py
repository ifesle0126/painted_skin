import oss2
import calendar
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
oss2_config = config['oss2']

access_key_id = oss2_config['access_key_id']
access_key_secret = oss2_config['access_key_secret']
endpoint = oss2_config['endpoint']
bucket_config = oss2_config['bucket']

auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_config)
# https://examplebucket.oss-cn-hangzhou.aliyuncs.com/example/example.jpg


def upload_img(img_names):
    img_urls = []
    for img_name in img_names:
        print("upload img " + img_name)
        obj_name = img_name.split("/")[-1]
        rst = bucket.put_object_from_file(
            'painted_skin_imgs/' + obj_name, img_name)
        img_url = "https://" + bucket_config + "." + \
            endpoint + "/painted_skin_imgs/" + obj_name
        img_urls.append(img_url)
        print("http status: {0}, request_id: {1}, img_url: {2}".format(
            rst.status, rst.request_id, img_url))
    return img_urls


if __name__ == "__main__":
    upload_img(["./img/inpaint_img_1692524194.png"])
