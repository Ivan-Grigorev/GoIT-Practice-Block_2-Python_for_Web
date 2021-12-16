app['my_priv_key'] = data


async def handler(request):
    data = request.app['my_priv_key']

# ChainMap config_dict
