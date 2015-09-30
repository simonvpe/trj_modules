import time

def run(args):
    ret = 0
    while ret < 5:
        print "Hello world %s" % str(args)
        time.sleep(1)
        ret = ret + 1
    return ret

if __name__ == "__main__":
    print run(None)

# TEST AGAIN
