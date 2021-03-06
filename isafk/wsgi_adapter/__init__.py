from werkzeug.wrappers import Request
import threading


# WSGI 调度框架入口
def wsgi_app(app, environ, start_response):
    # 解析请求头
    request = Request(environ)

    # 把请求传给框架的路由进行处理，并获取处理结果
    response = app.dispatch_request(request)

    # 返回给服务器
    return response(environ, start_response)
