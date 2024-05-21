season = ["winter", "spring", "summer", "autumn"]

def month_to_season():
    num_month = int(input("Num month: "))
    if num_month == 12 or num_month == 1 or num_month == 2:
        print(season[0])
    elif num_month == 3 or num_month == 4 or num_month == 5:
        print(season[1])
    elif num_month == 6 or num_month == 7 or num_month == 8:
        print(season[2])
    elif num_month == 9 or num_month == 10 or num_month == 11:
        print(season[3])
    else:
        print("Подумай еще раз, дружочек-пирожочек")


month_to_season()
