from ranges_gen import gen_ranges
from users_gen import gen_users
from find_ip import parse_ip
from interval_tree import IntervalTree, Segment


def ip_address(num):
    return '.'.join(map(lambda x: str((num >> 8 * x) & 255), reversed(range(4))))


def find_user_ranges_lazy(user_ip, segments):
    result = []
    for segment in segments:
        if segment.left <= user_ip <= segment.right:
            result.append(segment.name)
    return result


def test_random(range_num):
    print('test_random(%d)' % range_num)
    users = list(gen_users(1000, min_ip, max_ip))
    ranges = [Segment(*r) for r in gen_ranges(range_num, min_ip, max_ip)]
    tree = IntervalTree.build_tree(ranges)
    if not tree and range_num == 0:
        return
    for user, ip in users:
        res1 = [s.name for s in tree.find(ip)]
        res2 = find_user_ranges_lazy(ip, ranges)
        if sorted(res1) != sorted(res2):
            print('Error: [%s] != [%s]' % (','.join(res1), ','.join(res2)))
            print('User: %d\t%s\n' % (user, ip_address(ip)))
            with open('test\\failed_ranges.tsv', 'w+') as f:
                for s in ranges:
                    f.write('%s-%s\t%s\n' % (ip_address(s.left), ip_address(s.right), s.name))
            with open('test\\failed_transactions.tsv', 'w+') as f:
                f.write('%d\t%s\n' % (user, ip_address(ip)))
            exit()

if __name__ == '__main__':
    min_ip = parse_ip('10.10.0.0')
    max_ip = parse_ip('10.11.0.0')

    for i in range(10000):
        test_random(i)
