def get_sum(a, b):
    if a < b:
        i = a
        sum = 0
        while i <= b :
            sum += i
            i += 1
        return sum
    if a > b:
        i = b
        sum = 0
        while i <= a :
            sum += i
            i += 1
        return sum
    if a == b:
        return a

def main():
    print(get_sum(5, 10))

if __name__ == '__main__':
    main()
