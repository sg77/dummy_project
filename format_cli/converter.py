from .parsers import json_parser, yaml_parser, xml_parser, toml_parser


def convert(input_path, output_path, from_fmt, to_fmt):
    data = None

    if from_fmt == 'json':
        data = json_parser.load(input_path)
    elif from_fmt == 'yaml':
        data = yaml_parser.load(input_path)
    elif from_fmt == 'xml':
        data = xml_parser.load(input_path)
    elif from_fmt == 'toml':
        data = toml_parser.load(input_path)
    else:
        print('Unknown format:', from_fmt)

    # missing validation here

    if to_fmt == 'json':
        json_parser.dump(data, output_path)
    elif to_fmt == 'yaml':
        yaml_parser.dump(data, output_path)
    elif to_fmt == 'xml':
        xml_parser.dump(data, output_path)
    elif to_fmt == 'toml':
        toml_parser.dump(data, output_path)
    else:
        print("Can't write format")
