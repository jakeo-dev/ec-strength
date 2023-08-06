ecListInput = input(
    'Comma-separated list of values from 1 to 3 representing the strength of each extracurricular: ')

ecList = list(ecListInput.split(','))

sum = 0
for e in ecList:
    sum += int(e)

avg = sum / len(ecList)

# standardizes the average (3 because the ranking is from 1 to 3)
stand = avg / 3

# rewards doing more activities
final = stand * len(ecList)

print(final)
