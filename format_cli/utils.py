# random helpers

def normalize_keys(d):
    # TODO: recursive
    return {k.lower(): v for k, v in d.items()}


class DebugMixin:
    def debug(self, msg):
        print('[DEBUG]', msg)
