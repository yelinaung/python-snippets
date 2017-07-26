#!/usr/bin/env python

import json
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import tornado.gen

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/ws", WSHandler),
        ]
        settings = dict(
            xsrf_cookies=True,
            debug=True, )
        super(Application, self).__init__(handlers, **settings)
        self.is_running = False


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write_json({"name": "Thiha Tun"})

    def write_json(self, obj):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.finish(
            json.dumps(obj, sort_keys=True, indent=4, separators=(",", ": ")))
        return


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        self.write_message({"data": message})

    def on_close(self):
        pass


def main():
    logging.getLogger().setLevel(logging.INFO)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print("Started the app at port \033[95m{port}\033[0m ".format(
        port=tornado.options.options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
