class FormatPlaceholder:
    def __init__(self, key):
        self.key = key

    def __format__(self, spec):
        result = self.key
        if spec:
            result += ":" + spec
        return "{" + result + "}"

        
class FormatDict(dict):
    def __missing__(self, key):
        return FormatPlaceholder(key)
