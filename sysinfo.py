import platform
import json
import getpass

def run(data_file, args):
    print "Running sysinfo"
    print "data_file:%s" % str(data_file.data)
    print "args:%s" % str(args)
    data = {
        'machine'  : platform.machine(),
        'node'     : platform.node(),
        'platform' : platform.platform(),
        'processor': platform.processor(),
        'release'  : platform.release(),
        'system'   : platform.system(),
        'version'  : platform.version(),
        'user'     : getpass.getuser()
    }
    data_file.data = json.dumps(data, indent=4)
