import time

def run(args):
    while True:
        print "Hello world %s" % str(args)
        time.sleep(1)

if __name__ == "__main__":
    run(None)
