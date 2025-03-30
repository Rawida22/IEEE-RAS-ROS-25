first_set = {"A","B","c","6","D","e" }
second_set ={"6","A","D","5","F","10","G" }

def common_elements(first_set ,second_set):
   return first_set.intersection(second_set)

print(common_elements(first_set,second_set))