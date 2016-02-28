import time

from ranges_gen import gen_ranges
from users_gen import gen_users
from find_ip import parse_ip
from interval_tree import IntervalTree, Segment

if __name__ == '__main__':
    min_ip = parse_ip('5.0.0.0')
    max_ip = parse_ip('10.0.0.0')
    users = list(gen_users(1000, min_ip, max_ip))

    num = 256
    print('     %s  |    %s   |  %s' % ('ranges', 'build tree', 'find 1000 users'))
    for i in range(14):
        ranges = [Segment(*r) for r in gen_ranges(num, min_ip, max_ip)]
        start = time.time()
        tree = IntervalTree.build_tree(ranges)
        build_time = time.time() - start
        start = time.time()
        for user, ip in users:
            tree.find(ip)
        print('%10d   |   %10fs   |   %10fs' % (num, build_time, time.time() - start))
        num *= 2
