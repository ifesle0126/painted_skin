import configparser

import requests
import random
from hashlib import md5
import hanlp

HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)

section = "baidu_translate"


def translate(oriword,optimize=False):

    # Set your own appid/appkey.
    #从配置文件读取数据
    config = configparser.ConfigParser()
    config.read('config.ini')
    appid = config.get(section, 'appid')
    appkey = config.get(section, 'appkey')


    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'zh'
    to_lang = 'en'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = oriword

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    print("----------translate:", result)
    if optimize == False:
        return result['trans_result'][0]['dst']
    else:
        return optimize_promot(result['trans_result'][0]['dst'])

def optimize_promot(translate):
    '''
    优化提示词接口，目标将提示词进行优化以达到更好的效果
    :param self:
    :param translate:
    :return:
    '''

    n = HanLP(translate)
    print("----------optimize_promot:", n['tok/fine'])
    return ",".join(n['tok/fine'])
