# Uses python3

def gcd(num_1, num_2):

    if num_1 <= 0 or num_2 <= 0:
        raise ValueError('Inputs must be greater than zero')

    if num_1 > num_2:
        bigger, smaller = num_1, num_2
    else:
        bigger, smaller = num_2, num_1

    while True:
        remainder = bigger % smaller

        if remainder == 0:
            return smaller

        bigger, smaller = smaller, remainder

if __name__ == '__main__':
    n1 = input()
    nums = n1.split()

    print(gcd(int(nums[0]), int(nums[1])))