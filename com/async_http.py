#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', headers={'content-type': 'text/html'})


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), headers={'content-type': 'text/html'})


async def init(event_loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await event_loop.create_server(app_runner.server, '127.0.0.1', 5000)
    print('Server started at http://127.0.0.1:5000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
