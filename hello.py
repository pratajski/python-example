from __future__ import print_function
import sys


def hello(what):
    print('Hello hello, {}!'.format(what))


def say_what():
    return 'worldddd'


def main():
    hello(say_what())
    return 0


if __name__ == '__main__':
    sys.exit(main())
