#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import logging
import sys


def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            'hjkl',
            ['hello', 'jello', 'kello', 'lello']
        )
    except getopt.GetoptError as err:
        logging.exception(err)

    for opt, arg in opts:
        #print(opt)
        if opt in ('-h', '--hello'):
            print('hello')
        elif opt in ('-j', '--jello'):
            print('jello')
        elif opt in ('-k', '--kello'):
            print('kello')
        elif opt in ('-l', '--lello'):
            print('lello')

if __name__ == '__main__':
    main()
