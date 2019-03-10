import sys

from .test_multiphate import multiPhate

def main(arg=None):
    if args is None:
        arg = sys.argv[1:]
        multiPhate(args)

if __name__ == '__main__':
    sys.exit(main())
