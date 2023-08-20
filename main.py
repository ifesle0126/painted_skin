import web
import translator
import json
import img2img

urls = (
    '/', 'index',
    '/paint', 'paint'
)


class index:
    def GET(self):
        return "Hello, I am a robot!"

    def POST(self):

        return "Hello, I am a robot!"


class paint:
    def GET(self):
        # 获取get请求的参数
        data = web.input()
        print(data)
        ori_prompt = data['prompt']
        return translator.translate(ori_prompt, optimize=True)

    def POST(self):
        data = web.input()
        with open("./img/zzz.jpg", 'wb') as f:
            f.write(data.img)
        translate_prompt = translator.translate(data.prompt)
        urls = img2img.img2img("./img/zzz.jpg", translate_prompt)
        return urls


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
