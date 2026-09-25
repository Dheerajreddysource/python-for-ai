file=open("notes.txt","w")
file.write("i am learning python")
file.close()

file=open("notes.txt","w")
file.write("Name: Dheeraj \n"
"Branch: CSE \n"
"Goal: AI Engineer")
file.close()

file=open("notes.txt","w")
file.write("name:Rahul \n")
file.write("age:20\n")
file.close()

file=open("notes.txt","a")
file.write("Goal : AIe \n")
file.write("college : gnitc")
file.close()


file=open("notes.txt","r")

print(file.read())
file.close()

file=open("notes.txt","w")
file.write("Python\n")
file.write("C++\n")
file.write("AI")
file.close()

file=open("notes.txt","r")
print(file.read())

file.close()


with open("notes.txt","a") as file:
    file.write("\n machine learing")
    