#Q1: Write a code to check if a year is a leap year.
year= int(input('please enter a year\n'))

if year%100 !=0 and year%4==0 or year%400==0:
    print(f'year {year} is leap')
else :
    print(f'year {year} is NOT leap')
    
