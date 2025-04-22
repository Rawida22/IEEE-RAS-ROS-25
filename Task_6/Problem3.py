class Calculator:
    def add (self,A,B):
        return A+B
    def sub (self,A,B):
        return A-B
    def mul (self,A,B):
        return A*B
    def div (self,A,B):
        try:
            return A//B
        except ZeroDivisionError:
            return "Error Division by Zero!"
    
First_Calc = Calculator() 
print(First_Calc.add(10,5))   
print(First_Calc.sub(2,6)) 
print(First_Calc.mul(5,12))   
print(First_Calc.div(3,0)) 