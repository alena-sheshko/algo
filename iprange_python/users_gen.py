import argparse
import random
from find_ip import parse_ip


def ip_address(num):
    return '.'.join(map(lambda x: str((num >> 8 * x) & 255), reversed(range(4))))


def gen_users(num, min_ip, max_ip):
    for i in range(1, num + 1):
        yield i, random.randrange(min_ip, max_ip + 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Users generator.')
    parser.add_argument('quantity', type=int)
    parser.add_argument('--min', default='0.0.0.0',
                        help='min value of the generated ip address (e.g., --min 123.123.123.123)')
    parser.add_argument('--max', default='255.255.255.255',
                        help='max value of the generated ip address (e.g., --max 123.123.123.123)')

    args = parser.parse_args()
    if args.quantity <= 0:
        print('quantity has to be positive!')
        exit()

    with open('test\\transactions_%d.tsv' % args.quantity, 'w+') as f:
        for user_id, ip in gen_users(args.quantity, parse_ip(args.min), parse_ip(args.max)):
            f.write('%d\t%s\n' % (user_id, ip_address(ip)))