
def parse_range(range_str):
    pass


def parse_ip(ip_str):
    sum(map(lambda x: int(x[1]) << 8*x[0], enumerate(reversed(ip_str.split('.')))))


def parse_ip_file(filename):
    return []


def parse_range_file(filename):
    return []

if __name__ == '__main__':
    pass
