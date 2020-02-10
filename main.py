# alternative: low, high = (a, b) if a < b else (b, a)
#

def get_sum(a, b):
    low = None
    high = None
    if a < b:
        low = a
        high = b
    elif a > b:
        low = b
        high = a
    else:
        return a
    i = low
    sum = 0
    while i <= high:
        sum += i
        i += 1
    return sum


def main():
    print(get_sum(10, 20))
    print(get_sum(20, 10))
    print(get_sum(35, 15))


if __name__ == '__main__':
    main()

