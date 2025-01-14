# Employee management system

class Employee:
    def __init__(self, name, id, course, salary):
        self.name=name
        self.id=id
        self.course=course
        self.salary=salary
    def display_info(self):
        st = f'''Name: {self.name}
Employee id: {self.id}
Department: {self.course}
Salary: {self.salary}'''
        print(st)

    def update_info(self, name=None, course=None, salary=None):
        if name:
            self.name = name
        if course:
            self.course = course
        if salary:
            self.salary = salary

    def increment(self, percentage):
            self.salary += (percentage/100) * self.salary



class Employee_management():
     def __init__(self):
          self.reg = {}
    
     def add_employee(self, name, id, course, salary):
        if id in self.reg:
            print('Employee id already exist')
        else:   
            self.reg[id] = Employee(name, id, course, salary)
            print(f'Employee id {id} successfully created')
          
     def display_all_employee(self):
        for emp in self.reg:
             self.reg[emp].display_info()

     def increment_id(self, id, perc):
         if id not in self.reg:
             print('id not found')
         else:
            self.reg[id].increment(perc)


        

# main code
system = Employee_management()
system.add_employee("Ravi", 'gla3456', 'cse', 10000)
system.add_employee("Saket", 'gla34456', 'ece', 1000)

system.display_all_employee()

system.increment_id('gla34456', 10)

#this is python code