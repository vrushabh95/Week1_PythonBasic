year = int(input("Enter the year"))
if(len(str(year)) != 4):
    print("Enter only 4 digit")
else:
    if(year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("it is leap year")
            else:
                print("it is not leap year")
        else:
            print("it is leap year")
    else:
        print("it is not leap year")

