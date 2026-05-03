#problem 1
Sale_list = [50, 75, 150, 125, 100]
Week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

max_sale = max(Sale_list)
max_day = Week_list[Sale_list.index(max_sale)]

print(f"The Max sales is $ {max_sale}")
print(f"The Max sales day is {max_day}")