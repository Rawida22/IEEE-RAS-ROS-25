
#num = input("Enter your Numbers(-1 to stop):")
#numbers=list(map(int,num.split()))

#for x in num:
  #if x == -1:
 #  break

#print(f"{max(numbers),{min(numbers)}}")
numbers = []
print("Enter numbers one by one (enter -1 to stop):")

while True:
    user_input = input("> ")
    
    # Check first if input is -1
    if user_input.strip() == "-1":
        break
    num = int(user_input)
    numbers.append(num)

if numbers:
    print(f"Largest number: {max(numbers)}, Smallest number: {min(numbers)}")
else:
    print("No valid numbers were entered")