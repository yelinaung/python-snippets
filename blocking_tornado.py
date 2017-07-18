#!/usr/bin/env python
#
# Copyright 2017 99.co
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            blog_title=u"Tornado Blog",
            xsrf_cookies=True,
            debug=True, )
        super(Application, self).__init__(handlers, **settings)
        self.is_running = False


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # import pdb; pdb.set_trace()
        if self.application.is_running:
            self.write("Is running. Wait !")
        else:
            self.application.is_running = True
            result = yield self.reall_long_function()
            self.application.is_running = False
            self.write(result)

    @tornado.gen.coroutine
    def reall_long_function(self):
        """ Really long executing function """
        print("doing some heavy calculation")
        yield tornado.gen.sleep(5)
        print("about to be done")
        yield tornado.gen.sleep(2)
        result = "I am done"
        print(result)
        raise tornado.gen.Return(result)


def main():
    logging.getLogger().setLevel(logging.INFO)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    print("Starting the app ..")


if __name__ == "__main__":
    main()
