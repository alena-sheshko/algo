from median import mid_element, quick_sort


class Segment:
    def __init__(self, left, right, name):
        self.left = left
        self.right = right
        self.name = name

    def __le__(self, other):
        return self.left <= other.left


class IntervalTree:
    def __init__(self, segments):
        # get median element
        self.x_mid = mid_element(segments, 0, len(segments))
        left_child = []   # left subtree intervals
        right_child = []  # right  subtree intervals
        for s in segments:
            if s.right < self.x_mid:
                left_child.append(s)
            if s.left > self.x_mid:
                right_child.append(s)
            # x_mid overlaps
            if s.right >= s.left <= self.x_mid:
                self.left_segments.append(s)
                self.right_segments.append(s)
        quick_sort(self.left_segments, 0, len(self.left_segments))
        quick_sort(self.right_segments, 0, len(self.right_segments), lambda x, y: x.right >= y.right)
        # build subtrees
        self.left = IntervalTree(left_child) if left_child else None
        self.right = IntervalTree(right_child) if right_child else None

    def find(self, ip):
        # check subtrees
        if self.left and ip < self.x_mid:
            result = self.left.find(ip)
        if self.right and ip > self.x_mid:
            result = self.right.find(ip)
        # check x_mid overlaps
        if ip < self.x_mid:
            for s in self.left_segments:
                if ip < s.left:
                    break
                result.append(s)
        if ip >= self.x_mid:
            for s in self.right_segments:
                if ip > s.right:
                    break
                result.append(s)
        return result

    @staticmethod
    def build_tree(segments):
        if not segments:
            return None
        return IntervalTree(segments)

