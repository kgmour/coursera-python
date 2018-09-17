# Uses python3

def lcm(num_1, num_2):

    if num_1 < 1 or num_2 < 1:
        raise ValueError('Inputs must be greater than 0')

    if num_1 > num_2:
        bigger, smaller = num_1, num_2
    else:
        bigger, smaller = num_2, num_1

    while True:
        remainder = bigger % smaller

        if remainder == 0:
            break

        bigger, smaller = smaller, remainder

    result =  (num_1 * num_2) // smaller

    return int(result)

if __name__ == '__main__':
    nums = input()
    n1, n2 = nums.split()

    print(lcm(int(n1), int(n2)))