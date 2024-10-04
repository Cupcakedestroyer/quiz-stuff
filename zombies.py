zombies = int(input("initial amount of zombies"))
ppd = int(input("how many people get turned into zombies a day"))
days = int(input("how many days since mr.chatard was infected"))



for day in range(days):
    zombies = zombies +  (zombies * ppd)



print("this is how many zombies there are today", zombies )