import toml


def load(path):
    return toml.load(path)


def dump(data, path):
    with open(path, 'w') as f:
        toml.dump(data, f)

# missing edge case handling
