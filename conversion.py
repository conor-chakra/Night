weight = int(input('how much do you weigh in kilograms or pounds? '))
unit = input('(L)bs or (k)g: ')
if unit.upper() == 'L':
    0.45 * weight
    print(f'You are {weight} pounds')
else :
    0.45 / weight
    print(f'You are {weight} Kilograms')
    


birth_year = input('what is your birth year? ')
age = 2021 - int(birth_year)
year = f'{age} is your age'
print(year)
