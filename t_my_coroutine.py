#!/usr/bin/env python
# -*- coding: utf-8 -*-

# refer to http://www.liaoxuefeng.com/wiki
# /0014316089557264a6b348958f449949df42a6d3a2e542c000
# /001432090171191d05dae6e129940518d1d6cf6eeaaa969000


def producer():
    response = ''
    while True:
        # Just like this:
        # response = recv(request)
        # producer recieve a request from the consumer and give a response.
        # But need grammar 'yield' for generator
        request = yield response
        print('producer make response for request %s' % request)
        response = 'response for request ' + str(request)


def consumer(p):
    # Start the generator 'producer'.
    # This will make the producer stop at yield
    p.send(None)

    request_num = 5
    request = 0
    while request < request_num:
        request += 1
        print('consumer make request %s' % request)
        response = p.send(request)
        print('consumer get response(%s) of request %s' % (response, request))
    p.close()

p = producer()
consumer(p)
