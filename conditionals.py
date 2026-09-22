# GW, Conditionals Notes

miliatary_time = 900

if miliatary_time < 600:
    print("It 's to early why are you awake?!.")
elif miliatary_time < 900:
    print("Good Morning!")
elif miliatary_time < 1200:
    print("Good Morning! You should be at school!")
elif miliatary_time < 1700:
    print("Good Afternoon")
else:
    print("Good evening")

# nesting conditionals
day = "Saturday"
time = 900

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be at school")
    else:
        if time > 1200:
            print("Good Afternoon!")
        else:
            print("Good Morning")
else:
    print("You are not required to be at school")