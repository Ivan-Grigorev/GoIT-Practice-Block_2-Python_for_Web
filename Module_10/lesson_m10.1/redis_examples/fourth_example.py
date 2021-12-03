import json
import sys
import httpx
import redis


def get_info_from_api(name) -> dict:
    with httpx.Client() as web_client:
        base_url = "https://api.nationalize.io?name"

        url = f"{base_url}={name}"

        response = web_client.get(url)
        return response.json()['country'][0]['country_id']


def get_info_from_cache(name, client):
    """Data from redis."""

    val = client.get(name)
    return val


def set_info_to_cache(name, value, client):
    """Data to redis."""

    data = client.set(name, value)
    return data


def cash_analyzer(name, client):
    # First it looks for the data in redis cache
    data = get_info_from_cache(name, client)

    # If cache is found then serves the data from cache
    if data:
        print(f'{data.decode("utf-8")} and this country i took from cash')
    else:
        data = get_info_from_api(name)
        print(f'{data} and this country i took from api. Now im gonna cash it, try it later')
        # This block sets saves the response to redis and serves it directly
        if data:
            state = set_info_to_cache(name=name, value=data, client=client)
            return state


if __name__ == '__main__':
    redis_client = redis.Redis(host='localhost', port=6380, db=0)

    cash_analyzer('boris', redis_client)
    cash_analyzer('petr', redis_client)
