def octal_string_decode(num):
    num = int(num)
    result = 0
    power = 0
    while num > 0:
        result += (num % 10)*(8**power)
        power += 1
        num //= 10
    return result


if __name__ == '__main__':
    number = input()
    print(str(octal_string_decode(number)))
