#Uses python3

def get_fibonacci_number(n):
    number = int(n)
    if number <= 1:
        return number
    list_of_fibonacci_sequence = [0, 1]
    for i in range(2, number + 1):
        list_of_fibonacci_sequence.append(list_of_fibonacci_sequence[i-1] + list_of_fibonacci_sequence[i-2])
    return list_of_fibonacci_sequence[number]

if __name__ == '__main__':
    num = input()

    print(get_fibonacci_number(num))