import datetime
import pprint


# TODAY = datetime.datetime.today()
TODAY = datetime.datetime.fromisoformat("2030-12-14")
BIRTHDAY = datetime.datetime.fromisoformat("1996-12-14")
AGE = TODAY - BIRTHDAY
print(AGE)
DED_LOL = datetime.datetime.fromisoformat("2096-12-14")
LifeSpan = DED_LOL - BIRTHDAY
timeLeft = DED_LOL - TODAY

print(timeLeft)
PerCenct = AGE / LifeSpan * 100

income_per_day = 3334.89 / 16
income_per_hour = income_per_day / 24
print(income_per_hour)


expense = {
    "bad": 2000,
    "rightnow": 3300,
    "good": 4000,
    "hellyeah": 6000,
}

NET = 7656.78

GOAL = timeLeft.days * expense["good"] / 30

# pprint.pprint("Gold money: $: "+str(GOAL))
pprint.pprint("Bad Gold: $" + str(timeLeft.days * expense["bad"] / 30))
pprint.pprint("Right Now Gold: $" + str(timeLeft.days * expense["rightnow"] / 30))
pprint.pprint("good Gold: $" + str(timeLeft.days * expense["good"] / 30))
pprint.pprint("Hell Yeah Gold: $" + str(timeLeft.days * expense["hellyeah"] / 30))
