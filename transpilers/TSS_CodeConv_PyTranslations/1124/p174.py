class p174:
    @staticmethod
    def main(args):
        print((p174()).run())
    _SIZE_LIMIT = 1000000
    _TYPE_LIMIT = 10
    def run(self):
        type = [0 for _ in range(p174._SIZE_LIMIT + 1)]
        n = 3
        while (n - 1) * 4 <= p174._SIZE_LIMIT:
            for m in range(n - 2, 0, -2):
                tiles = n * n - m * m
                if tiles > p174._SIZE_LIMIT:
                    break
                type [tiles] += 1
            n += 1
        count = 0
        for t in type:
            if 1 <= t and t <= p174._TYPE_LIMIT:
                count += 1
        return str(count)
