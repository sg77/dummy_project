import yaml


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def dump(data,path):
  with open(path,'w') as f:
      yaml.dump(data,f)

# inconsistent indent above intentionally
