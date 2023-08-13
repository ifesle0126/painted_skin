import web
import translator

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
        data = web.data()
        return translator.translate(data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
