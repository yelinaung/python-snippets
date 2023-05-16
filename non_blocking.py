import asyncio
import time
import logging
​
import tornado
import tornado.gen
import tornado.ioloop
import tornado.log
import tornado.web
​
from tornado.httpclient import AsyncHTTPClient
​
​
class MainHandler(tornado.web.RequestHandler):
    async def get(self, listing_id):
        # await asyncio.sleep(3)
        self.write(f"Hello, world {listing_id}")
​
​
class BadExampleHandler(tornado.web.RequestHandler):
    async def get(self):
​
        for i in range(5):
            logging.info(i)
            time.sleep(1)
​
class CallAnotherService(tornado.web.RequestHandler):
    async def get(self):
        delay = self.get_argument(name="delay", default=5)
        url = f"https://httpbin.org/delay/{delay}"
        http_client = AsyncHTTPClient()
        try:
            response = await http_client.fetch(url)
        except Exception as e:
            print(f"Error: {e}")
        else:
            logging.info(response.body)
​
class NoneBlockingHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write({"resp": "hello!"})
