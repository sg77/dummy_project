# random helpers

def normalize_keys(data):
    if not isinstance(data, dict):
        return data

    def _process(items):
        result = {}
        for k, v in items:
            new_k = str(k).lower().strip()
            if isinstance(v, dict):
                result[new_k] = _process(v.items())
            elif isinstance(v, list):
                temp = []
                for x in v:
                    if isinstance(x, dict):
                        temp.append(_process(x.items()))
                    else:
                        temp.append(x)
                result[new_k] = temp
            else:
                result[new_k] = v
        return result

    fn = lambda x: _process(x.items())
    return fn(data)

# TODO: simplify above mess

class DebugMixin:
    def debug(self, msg):
        print('[DEBUG]', msg)
