# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    last_num_dict = {0: 0, 1: 1}

    for i in range(2, n + 1):
        last_num_dict[i] = (last_num_dict[i - 1] + last_num_dict[i - 2]) % 10

    return last_num_dict[n]

if __name__ == '__main__':
    num = input()
    n = int(num)
    print(get_fibonacci_last_digit_naive(n))
