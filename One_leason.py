# Classes and instances

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

#print(emp_1)
#print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@gmail'
emp_1.pay = '50000'

emp_2.first = 'Alexandre'
emp_2.last = 'Oliveira'
emp_2.email = 'oliveira.alexandre@gmail'
emp_2.pay = '80000'

#print(emp_1.email)
#print(emp_2.email)

class Employee_Home:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee_Home('Corey', 'Schafer', 50000)
emp_2 = Employee_Home('Alexandre', 'Oliveira', 80000)
print(Employee_Home.fullname())


#print(emp_1.email)
#print(emp_2.email)
#print(emp_1.fullname)   
#print(emp_2.fullname())     

