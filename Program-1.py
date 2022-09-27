# This class will take a, b and type of operation as attributes and give the result of the operation
class Operation:

    def __init__(self, a, b, op):
        self.num1 = a
        self.num2 = b
        self.operation = op

    # this method will actually perform the operation by comparing the type of operation 
    def main_op(self):
        if self.operation.lower() == "addition":
            return self.num1 + self.num2
        elif self.operation.lower() == "substraction":
            return self.num1 - self.num2
        elif self.operation.lower() == "multiplication":
            return self.num1 * self.num2
        elif self.operation.lower() == "division":
            return self.num1 / self.num2
        

print("Welcome!! This is a Calculator.")
first_number_a = float(input(f"Enter the first number a = "))
second_number_b = float(input(f"Enter the second number b = "))
type_of_operation = input("Enter the type of operation operation to perform. For eg. 'Addition' : ")

result = Operation(first_number_a, second_number_b, type_of_operation)

print(f"The result of the {type_of_operation} of {first_number_a} and {second_number_b} is : {result.main_op()}")
