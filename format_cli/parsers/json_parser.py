import json


def load(path):
  with open(path) as f:
    return json.load(f)

def dump(data, path):
  with open(path, 'w') as f:
    json.dump(data, f, indent=2)

# TODO: streaming support
