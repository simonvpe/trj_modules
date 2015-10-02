import platform
import json

def run(f, args):
    data = {
        'machine'  : platform.machine(),
        'node'     : platform.node(),
        'platform' : platform.platform(),
        'processor': platform.processor(),
        'release'  : platform.release(),
        'system'   : platform.system(),
        'version'  : platform.version()
    }
    f.data = json.dumps(data)
