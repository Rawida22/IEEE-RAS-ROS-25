import math
num = int(input("Enter a number: "))
sum = 0
i_nums=[]
if num <0 :
 print("Negative numbers is not valid")
elif num==0:
 print("Not valid for 0")
else:
 for i in range(2,num+1,2):
  sum = sum +i
  i_nums.append(i) 
print(f"The sum of even numbers from 1 to {num} is {sum} ({' + '.join(map(str, i_nums))})")