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





