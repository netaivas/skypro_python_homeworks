def bank():
    ar_1 = int(input("Sum: "))
    ar_2 = int(input("Period: "))
    percent = 1.1
    sum = ar_1 * percent ** ar_2
    print(round(sum))


bank()
