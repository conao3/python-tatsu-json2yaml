import argparse
import logging

from . import lib


logger = logging.getLogger(__name__)


def repl() -> None:
    while True:
        try:
            line = input('json2yaml> ')
            res = lib.main.rep(line)
            if res:
                print(res)

        except EOFError:
            break

        except Exception:
            logger.exception('Error')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Convert JSON to YAML')
    parser.add_argument('-i', '--input', help='Input JSON file')

    return parser.parse_args()


def main():
    args = parse_args()

    if not args.input:
        repl()
        return

    with open(args.input) as f:
        inpt = f.read()

    print(lib.main.rep(inpt))
