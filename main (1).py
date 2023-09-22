input_year=int(input("Enter a year:"))
def is_leap(year):
     if (year % 400  ==0) or (year % 4==0 and year % 100  !=0):
      return

      return 
if is_leap(input_year):
      print("it is a leap year")
else:
     print("it is not a leap year")