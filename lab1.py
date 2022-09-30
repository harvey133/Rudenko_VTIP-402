def main():
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))
        c = int(input('Введите С: '))
        d = int(input('Введите D: '))
        if x >= 5:
            y = ((a ** 2) * c + (b ** 2) * d) / x
        else:
            y = ((x ** 2 ) + 5 )
        print("y = %.1f" % y)
    except:
        print("Неверные данные!")
if __name__ == '__main__':
    main()
