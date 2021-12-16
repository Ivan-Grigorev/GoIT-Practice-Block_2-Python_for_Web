from aiohttp import web


async def handler(request):
    print("Handler function called")
    return web.Response(text="Hello")


@web.middleware
async def middleware1(request, handler):
    print('Middleware 1 called')
    response = await handler(request)
    print('Middleware 1 finished')
    return response


@web.middleware
async def middleware2(request, handler):
    print('Middleware 2 called')
    response = await handler(request)
    print('Middleware 2 finished')
    return response

app = web.Application(middlewares=[middleware2, middleware1])
app.router.add_get('/', handler)
web.run_app(app)
