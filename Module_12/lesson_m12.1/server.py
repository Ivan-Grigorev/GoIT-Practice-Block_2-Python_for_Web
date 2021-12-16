from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', 'Anonym')
    text = f"Hello, {name}"
    return web.Response(text=text)


app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
])


if __name__ == '__main__':
    web.run_app(app)


# Request
# read() -> bytes
# text() -> str
# json() -> dict
# multipart()

# Response
# status (200 Success)
# headers
# cookies

# body - byte
# text - str
# WebSocketResponse - send_str(), receive()

# web.HTTPException

