def is_leap(year):
    leap = False
    if (year % 4 != 0):
        leap = False

    elif ((year % 100 == 0)& (year % 400 != 0)):
        leap = False
    elif (year % 100 == 0 & year % 400 == 0):
        leap = True

    # Write your logic here

    return leap
year = int(input())
print(is_leap(year))