import asyncio, aiohttp

apiurl = ""
BearerToken = ""
headers = {"Authorization": f"Bearer {BearerToken}"}

class PhigrosUnlimitedAPI:
    def __init__(self) -> None:
        pass
        
    async def _user_best19(SessionToken:str, overflow:int = 0, withsonginfo:bool = False):
        url = apiurl + f"user/best19?SessionToken={SessionToken}&overflow={overflow}&withsonginfo={withsonginfo}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=headers)as reqs:
                    return await reqs.json()
        except Exception as e:
            return f'Error {type(e)}'
        
    async def _user_best(SessionToken:str, songid:str, level:str = "IN", withsonginfo:bool = False):
        url = apiurl + f"user/best?SessionToken={SessionToken}&songid={songid}&level={level}&withsonginfo={withsonginfo}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=headers)as reqs:
                    return await reqs.json()
        except Exception as e:
            return f'Error {type(e)}'

    async def _song_info(songid:str):
        url = apiurl + f"song/info?songid={songid}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url)as reqs:
                    return await reqs.json()
        except Exception as e:
            return f'Error {type(e)}'
        
    async def _song_random():
        url = apiurl + f"song/random"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url)as reqs:
                    return await reqs.json()
        except Exception as e:
            return f'Error {type(e)}'
