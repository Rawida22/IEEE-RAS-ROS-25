
num = int(input("Enter number: "))
fact = 1
ss = range(1, num + 1)
if num < 0:
    print(" does not exist for neg nums")
elif num == 0:
    print("The factorial is 1")
else:
    for i in ss:
        fact *= i
    i_nums = ' * '.join(map(str, ss)) 
    print(f"The factorial of {num} is {fact} ({i_nums[::-1]})")
