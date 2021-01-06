import math

family_income = round(float(input()), 2)
average_grade = round(float(input()), 2)
minimal_wage = round(float(input()), 2)

scholarship = 0
excellent_results = 0

if average_grade > 4.5 and family_income < minimal_wage:
    scholarship = math.floor(minimal_wage * 0.35)

if average_grade >= 5.5:
    excellent_results = math.floor(average_grade * 25)

if scholarship == 0 and excellent_results == 0:
    print("You cannot get a scholarship!")
else:
     if scholarship > excellent_results:
         print(f"You get a Social scholarship {scholarship} BGN")
     else:
         print(f"You get a scholarship for excellent results {excellent_results} BGN")
