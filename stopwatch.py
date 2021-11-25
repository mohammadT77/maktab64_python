import datetime
import time

if __name__ == '__main__':
    t0 = datetime.datetime.now()
    try:
        while True:
            t = datetime.datetime.now()
            print((t-t0).seconds)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Finished!")
