import argparse
from datetime import datetime, timedelta, time, date
from time import sleep

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Countdown example')

    parser.add_argument('target_time', nargs='?', type=time.fromisoformat, metavar='TARGET',
                        help='target_time to countdown')
    parser.add_argument('-ho', '--hour', type=int, metavar='H', default=0, help='hours to countdown')
    parser.add_argument('-m', '--min', type=int, metavar='M', default=0, help='minutes to countdown')
    parser.add_argument('-s', '--sec', type=int, metavar='S', default=0, help='seconds to countdown')

    args = parser.parse_args()

    if args.target_time:
        target_time = datetime.fromisoformat(f"{date.today()} {args.target_time}")
    else:
        target_time = datetime.now() + timedelta(hours=args.hour, minutes=args.min, seconds=args.sec)

    try:
        while True:
            td = target_time - datetime.now()
            if td <= timedelta():
                print("Times Up!")
                break
            print(td)
            sleep(1)

    except KeyboardInterrupt:
        print(f'\nKeyboardInterrupt: {target_time - datetime.now()} remaining.')