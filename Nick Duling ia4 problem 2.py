#Promblem 2
num_list = []
value = float(input("Enter value: "))
if value != 0:
    num_list.append(value)

value = float(input("Enter value (or 0 to end): "))
if value != 0:
    num_list.append(value)

value = float(input("Enter value (or 0 to end): "))
if value != 0:
    num_list.append(value)

value = float(input("Enter value (or 0 to end): "))
if value != 0:
    num_list.append(value)

print(num_list)

range_value = max(num_list) - min(num_list)

print("Range=", range_value)