#Uses python3

def max_pairs(length, values):
    if int(length) < 2:
        raise(IndexError)

    nums = [int(t) for t in values.split()]

    max_1_index = nums.index(max(nums))
    max_1 = nums[max_1_index]
    del nums[max_1_index]
    max_2 = max(nums)
    return max_1 * max_2

if __name__ == '__main__':
    length = input()
    values = input()

    print(max_pairs(length, values))