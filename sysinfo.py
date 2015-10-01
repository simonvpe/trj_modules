import platform

def run(args):
    return {
        'machine'  : platform.machine(),
        'node'     : platform.node(),
        'platform' : platform.platform(),
        'processor': platform.processor(),
        'release'  : platform.release(),
        'system'   : platform.system(),
        'version'  : platform.version()
    }

if __name__ == "__main__":
    print run(None)
