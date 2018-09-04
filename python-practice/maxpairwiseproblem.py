#Uses python3

def max_pairs(length, values):
    if int(length) < 2:
        raise(IndexError)

    nums = [int(t) for t in values.split()]

    max_1 = max(nums)
    max_2 = max([t for t in nums if t != max_1])
    return max_1 * max_2

if __name__ == '__main__':
    length = input()
    values = input()

    print(max_pairs(length, values))