repositary={
    "name":"python-for-ai",
    "language":"python",
    "files":["hello.py","README.md","main.py"],
    "author":"Dheeraj"
    }
print(repositary["name"])
print(repositary["language"])
print(repositary["author"])
repositary["version"]="V1"
print(repositary)

Company={
    "name":"J.P. Morgan",
    "location":"New York",

    "employees":[
        { 
            "name":"John Doe",
            "role":"Software Engineer",
            "skills":["Python","Java","C++"],
        },
        {
        "name":"Jane Smith",
        "role":"Data Scientist",
        "skills":["Python","R","SQL"],
        }
    ]
}
print(Company["name"])
print(Company["employees"][0]["name"])
print(Company["employees"][1]["skills"][0])
Company["employees"][0]["skills"].append("javascript")
Company["employees"][1]["role"]="Senior Data Scientist"
for employee in Company["employees"]:
    print(employee["name"] + " - " + employee["role"])
    print(employee.get("salary","not available"))    




laptop = {
    "brand": "Apple",
    "model": "MacBook Pro",
    "processor": "M1 Pro",
    "ram": 16
}

print(laptop.get("processor"))
laptop.update(
    {"storage":512,
     "ram":32,
    }
)

for key in laptop.keys():
    print(key)

for value in laptop.values():
    print(value)

for key,value in laptop.items():
    print(key,":",value)

remove=laptop.pop("ram")
print(remove)
laptop.setdefault("gpu","integrated")
print(laptop)

language=["Python","C","C++"]
print(language[0])
language[1]="Java"
language.append("Javascript")
language.insert(1,"HTML")
language.remove("HTML")
language.append("SQL")
print(len(language))
for x in language:
    print(x)


numbers=[10,20,30,40,50,60]
print(numbers[-1])
print(numbers[:3])
print(numbers[2:5])
numbers_copy=numbers.copy()
numbers_copy.append(70)
print(numbers)
print(numbers_copy)
squares=[number*number for number in numbers]
print(squares)
number=[5,10,15,20,25,30,35,40]
even_numbers=[x for x in numbers if x%2==0]
greater_than_20=[y for y in numbers if y>20]
squares=[number*number for number in numbers ]

Numbers=[3,8,11,16,21,24,29,32]
Even_numbers=[a for a in Numbers if a%2==0]
Odd_numbers=[b for b in Numbers if b%2!=0]
Even_squares=[z*z for z in Numbers if z%2==0]

student=("Dheerej",19,"CSE","GNITC")
name,age,branch,college=student
print(student[0])
print(student[-1])
print(student[:3])
for key in student:
    print(key)
print(name)
print(age)  
print(branch)
print(college)  

python_students = {"Rahul", "Arjun", "Kiran", "Dheeraj"}
cpp_students = {"Arjun", "Kiran", "Ravi", "Suresh"}
python_students.add("Vikram")
cpp_students.discard("Ravi")
print(python_students & cpp_students)
print(python_students - cpp_students)
print(python_students|cpp_students)
if "Dheeraj" in python_students:
    print("found")
ps=["Rahul", "Arjun", "Kiran", "Dheeraj","Arjun", "Kiran", "Ravi", "Suresh"] 
pp=set(ps)  


def claculate_square(number):
    return number*number
result=claculate_square(12)
print(result)

def calculate_billprice(price,quantity,discount=0):
    total=price*quantity
    final_price=total-discount
    return final_price
print(calculate_billprice(500,2))
print(calculate_billprice(500,2,100))


numbers=[11, 24, 35, 42, 57, 60]
def filter_even(numbers):
    return [x for x in numbers if x%2==0]
result=filter_even(numbers)
print(result)

def calculate(a,b):
    return(a+b,a-b,a*b)
addition, subtraction, multiplication = calculate(10, 5)
print(addition)
print(subtraction)
print( multiplication)

def check_number(number):
    if number > 0:
        return "postive"
    elif number<0:
        return "negative"
    else:
        return"zero"
print(check_number(10))
print(check_number(-5))
print(check_number(0))    

def check_age(age):
    if age < 13:
        return "Child"
    elif  13 < age <17:
        return "Teenager"
    elif 18 <=age <59:
        return "Adult"
    else: 
        return "Senior"
print(check_age(10))
print(check_age(16))
print(check_age(25))
print(check_age(65))   


def calculate_sum(*numbers):
    return sum(numbers)
print(calculate_sum(10, 20))
print(calculate_sum(5, 10, 15, 20))
print(calculate_sum(1, 2, 3, 4, 5))  
def show(*items):
    print(items)
show("Python", "C++", "Java", "SQL")           
def student_info(**details):
    for key, value in details.items():
       print(key,":",value)
student_info(name="Dheeraj", age=19, branch="CSE")



    
    