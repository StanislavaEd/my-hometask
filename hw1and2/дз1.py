necessityEnvelop = 0
freedomEnvelop = 0
educationEnvelop = 0
longTermEnvelop = 0
playEnvelop = 0
giveEnvelop = 0
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05
expectedIncome = 1000
message = (
    f"Hello.\n"
    f"We gonna fill your envelops by the money you input here!\n "
    f"Please input your amounts of money income and see the results.\n "
    f"Press Ctrl+c to exit script.\n"
    f" Enter the amount please:"
)
print (message)
sum = 0
while (sum < expectedIncome):
    line = int(input())
    sum += line

    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate
line = int(input())
`message = (
    f"\n Enter the amount please:"
)
print(message)`
message = (
    f"At the end we have:\n"
    f"Necessity Envelop has:{necessityEnvelop}.\n "
    f"Financial Freedom Envelop has:{freedomEnvelop}.\n"
    f"EducationEnvelop:{educationEnvelop}.\n"
    f"Play Envelop has:{playEnvelop}.\n"
    f"Give Envelop has:{giveEnvelop}.\n "
    f"Long Term Saving for Spending Envelop has:{longTermEnvelop}.\n"
    f"_______________________________________________________________.\n"
    f"Thanks for using our software :)"
)
print (message)
