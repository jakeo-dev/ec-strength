maxValue = int(input(
    'Maximum possible value for an extracurricular: '))
ecListInput = input(
    'Comma-separated list of values from 1 to ' + str(maxValue) + ' representing the strength of each extracurricular: ')

ecList = list(ecListInput.split(','))

sum = 0
for e in ecList:
    sum += int(e)

avg = sum / len(ecList)

# standardizes the average (maxValue because the ranking is from 1 to maxValue)
stand = avg / maxValue

# rewards doing more activities
final = stand * len(ecList)

print(final)
