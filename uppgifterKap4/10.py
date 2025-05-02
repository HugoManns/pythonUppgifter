# förklara vad koden nedan gör

for i in range(100):
    if i in (5, 7, 8):
        continue
    if i > 10:
        break
    print(i)
else:
    print("We are done")

# Koden räknar från 0 - 100
# om i är större än 10 så avslutar den räkningen och printar ut 0 - 10
# om talet inte är 5 7 eller 8 och inte större än 10 så printar den ut "We are done"