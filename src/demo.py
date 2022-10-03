def main():
    year = int(input("Enter the start year:\n"))
    start_day = int(input("Enter the start day in january:\n"))
    interval = int(input("Enter the interval:\n"))
    date = [start_day, 1, year]

    current_year = date[2]
    while date[2] == current_year:
        print(f"{date[0]}/{date[1]}/{date[2]} ")
        date = get_next_date(date, interval)


def get_next_date(date: list, interval: int):
    days = days_in_month(date[1], date[2])
    current = date[0]
    new = current+days
    date[0] = new
    while date[0] > days:
        date[1] = date[1] + 1
        date[0] = date[0] - days
        days = days_in_month(date[1], date[2])
        if(date[1]==13):
            date[1]=1
            date[2]=date[2]+1

    
    return date
    

def is_leap_lear(year: int):
    return year%400 == 0 or (year%4 == 0 and year%100 != 0)

def days_in_month(month: int, year: int):
    thirty1 = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]

    if month in thirty1: return 31
    elif month in thirty: return 30
    elif month==2:
        return 29 if is_leap_lear(year) else 28


def main2():
    print("sdgfg".fi)

if __name__=="__main__":
    main2()