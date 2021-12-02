# put your python code here
year = int(input())
if year % 400 == 0:
    print("Leap")
else:
    if year % 100 == 0:
        print("Ordinary")
    else:
        if year % 4 == 0:
            print("Leap")
        else:
            print("Ordinary")
