import sys
# test functionality of import module in poetry
# import aiohttp
# import asyncio
# import requests

from dev_demo import main

if __name__ == "__main__":
    # print(requests.get('https://api.github.com/events'))
    # print(aiohttp.ClientSession())
    # print(asyncio.get_event_loop())
    args: list[str] = sys.argv[1:]
    main(args)
