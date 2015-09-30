import time

def run(args):
    i = 0
    while i < 5:
        print "Hello world %s" % str(args)
        time.sleep(1)
        i = i + 1

if __name__ == "__main__":
    run(None)

# TEST AGAIN
