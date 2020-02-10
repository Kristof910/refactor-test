# alternative: low, high = (a, b) if a < b else (b, a)
# alternative: put the while in a range

def get_sum(a, b):
    if a == b:
        return a
    low, high = (a, b) if a < b else (b, a)
    return sum(range(low, high + 1))


def main():
    print(get_sum(10, 20)) #165
    print(get_sum(35, 15)) #525


if __name__ == '__main__':
    main()

