
numbers = []
print("Enter numbers one by one (enter -1 to stop):")

while True:
    user_input = input("> ")
    if user_input.strip() == "-1":
        break
    num = int(user_input)
    numbers.append(num)

if numbers:
    print(f" {max(numbers)}, {min(numbers)}")
else:
    print("No valid numbers were entered")
