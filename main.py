count = int(input("How many numbers would you like to compare?"))
max_num = float('-inf')
for i in range(count):
    number = int(input(f"Enter number {i+1}:"))
    if number >= max_num:
        max_num = number

print(f"The largest numbers is: {max_num}")