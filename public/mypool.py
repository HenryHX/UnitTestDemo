#!/usr/bin/env python
# encoding: utf-8

import threadpool



class MyPool(object):
    def __init__(self, func, poolsize=10, data=None):
        self.func = func
        self.poolsize = poolsize
        self.data = data

    def run(self):
        pools = threadpool.ThreadPool(self.poolsize)
        res_list = []
        # this will be called each time a result is available
        # result 为testsuit 保存py文件中的testcase
        def handle_result(request, result):
            print "**** Result from request #%s: %r" % (request.requestID, result)
            res_list.append(result)

        # this will be called when an exception occurs within a thread
        # this example exception handler does little more than the default handler
        def handle_exception(request, exc_info):
            if not isinstance(exc_info, tuple):
                # Something is seriously wrong...
                print request
                print exc_info
                raise SystemExit
                LOGGER.info("**** Exception occured in request #%s: %s" % \
                  (request.requestID, exc_info))

        reqs = threadpool.makeRequests(callable_=self.func, args_list=self.data, callback=handle_result,
                                       exc_callback=handle_exception)
        [pools.putRequest(req) for req in reqs]
        pools.wait()
        return res_list