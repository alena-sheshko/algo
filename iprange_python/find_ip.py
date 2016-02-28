import argparse
from interval_tree import Segment, IntervalTree


def parse_range(range_str, name):
    return Segment(*map(parse_ip, range_str.split('-')), name)


def parse_ip(ip_str):
    return sum(map(lambda x: int(x[1]) << 8 * x[0], enumerate(reversed(ip_str.split('.')))))


def parse_user_file(filename):
    users = []
    with open(filename) as f:
        for l in f:
            values = l.split('\t')
            users.append((values[0], parse_ip(values[1])))
    return users


def parse_range_file(filename):
    segments = []
    with open(filename) as f:
        for l in f:
            segments.append(parse_range(*l.rstrip().split('\t')))
    return segments

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find user networks.')
    parser.add_argument('range_file')
    parser.add_argument('user_file')
    parser.add_argument('output_file')

    args = parser.parse_args()
    tree = IntervalTree.build_tree(parse_range_file(args.range_file))
    if not tree:
        print('Range file is empty!')
        exit()

    with open(args.output_file, 'w+') as output:
        for user, ip in parse_user_file(args.user_file):
            res = tree.find(ip)
            if res:
                output.write('%s\t%s\n' % (user, ','.join(map(lambda x: x.name, res))))
            else:
                output.write('%s\tnot found\n' % user)


