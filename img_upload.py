import oss2
import calendar
import time
import configparser

config = configparser.ConfigParser()
oss2_config = config['oss2']

access_key_id = oss2_config['access_key_id']
access_key_secret = oss2_config['access_key_secret']
endpoint = oss2_config['endpoint']
bucket = oss2_config['bucket']

auth=oss2.Auth(access_key_id, acess_key + secret)
bucket = oss2.Bucket(auth, endpoint, bucket)
# https://examplebucket.oss-cn-hangzhou.aliyuncs.com/example/example.jpg


def upload_img(img_name):
	upload_img_name = img_name + calendar.timegm(time.gmtime())
	rst = bucket.put_object_from_file('./painted_skin_imgs/' + img_name, upload_img_name)
	print("http status: {0}, request_id: {1}, img: {2}".format(rst.status, rst.request_id, upload_img_name))
	return "https://myadrea-bucket.oss-cn-beijing-internal.aliyuncs.com/painted_skin_imgs/upload_img_name.jpg"