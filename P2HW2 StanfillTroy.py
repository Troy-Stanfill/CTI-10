#Troy Stanfill
#10/1/26
# Grading course of modules


Module1 = float(input("Please input grade for module 1: "))
Module2 = float(input("Please input grade for module 2: "))
Module3 = float(input("Please input grade for module 3: "))
Module4 = float(input("Please input grade for module 4: "))
Module5 = float(input("Please input grade for module 5: "))
Module6 = float(input("Please input grade for module 6: "))


belt = [Module1, Module2, Module3, Module4, Module5, Module6]

lowest_grade = min(belt)

highest_grade = max(belt)

Sum_of_grades = sum(belt)

Average = sum(belt) / len(belt)

print("--------Results------------")

print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Average:   {Average:.1f}")
print(f"Sum of grades   {Sum_of_grades:.2f}")
