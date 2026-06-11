import argparse
from .converter import convert


def main():
    parser = argparse.ArgumentParser(description='Convert file formats')
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--from', dest='from_fmt')
    parser.add_argument('--to', dest='to_fmt')

    args = parser.parse_args()

    # TODO: infer format better
    from_fmt = args.from_fmt or args.input.split('.')[-1]
    to_fmt = args.to_fmt or args.output.split('.')[-1]

    convert(args.input, args.output, from_fmt, to_fmt)

if __name__ == '__main__':
    main()
