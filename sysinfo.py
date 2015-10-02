import platform
import json

def run(f, args):
    print f
    print f.data
    data = {
        'machine'  : platform.machine(),
        'node'     : platform.node(),
        'platform' : platform.platform(),
        'processor': platform.processor(),
        'release'  : platform.release(),
        'system'   : platform.system(),
        'version'  : platform.version()
    }
    f.data = json.dumps(data, indent=4)
