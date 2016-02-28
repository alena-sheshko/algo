import argparse
import random
from find_ip import parse_ip


def ip_address(num):
    return '.'.join(map(lambda x: str((num >> 8 * x) & 255), reversed(range(4))))


def gen_ranges(num, min_ip, max_ip):
    for i in range(1, num + 1):
        ip1 = random.randrange(min_ip, max_ip + 1)
        ip2 = ip1 + random.randrange(256)
        if ip2 > max_ip:
            ip2 = max_ip
        yield ip1, ip2, 'Network%d' % i

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ranges generator.')
    parser.add_argument('quantity', type=int)
    parser.add_argument('--min', default='0.0.0.0',
                        help='min value of the generated ip address (e.g., --min 123.123.123.123)')
    parser.add_argument('--max', default='255.255.255.255',
                        help='max value of the generated ip address (e.g., --max 123.123.123.123)')

    args = parser.parse_args()
    if args.quantity <= 0:
        print('quantity has to be positive!')
        exit()

    with open('test\\ranges_%d.tsv' % args.quantity, 'w+') as f:
        for ip1, ip2, name in gen_ranges(args.quantity, parse_ip(args.min), parse_ip(args.max)):
            f.write('%s-%s\t%s\n' % (ip_address(ip1), ip_address(ip2), name))

