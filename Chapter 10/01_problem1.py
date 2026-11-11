# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer :
    company_name = "Microsoft"

    def __init__(self,emp_id, name, email):
        self.emp_id =  emp_id
        self.name  = name 
        self.email = email


p1 = Programmer("EMP01","First employee", "emp1@microscoft.com")
p2 = Programmer("EMP02","Second employee", "emp2@microscoft.com")
p3 = Programmer("EMP03","Third employee", "emp3@microscoft.com")

print(p1.emp_id, p1.email, p1.company_name, p1.name)
print(p2.emp_id, p2.email, p2.company_name, p2.name)
print(p3.emp_id, p3.email, p3.company_name, p3.name)