import web
import translator
import json

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
        #获取get请求的参数
        data = web.input()
        print(data)
        ori_prompt = data['prompt']
        return translator.translate(ori_prompt, optimize=True)

    def POST(self):
        request = web.input(data={})
        print(request.data)
        with open("./img/zzz.jpg", 'wb') as f:
            f.write(request.data.img.read())
        # json_data = json.loads(data)
        # ori_prompt = json_data['prompt']
        print(data.prompt)
        # return translator.translate(ori_prompt)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
