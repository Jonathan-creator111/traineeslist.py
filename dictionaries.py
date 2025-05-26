#Dictionaries
student = {
    "name":"Alex",
    "age":30,
    "email":"alex@gmail.com",
    "name":"Brian"
    }
print(type(student))
print(student)
#accessing values in a Dictionary
# use a key to display value
print(student["age"])
print(student["email"])
#name
print(student["name"])
#modify
student["age"]=40
print(student)
#modify name
student["name"]="Jonathan"
#add
student["phone"]="0742670714"
print(student)
#occupation
student["occupation"]="Doctor"
print(student)

student["location"]={"town":"nakuru","address":1020,"street":"kimathi"}
print(student)
#display kimathi
print(student["location"]["street"])

student["skills"]=["coding","teamplayer","leardership"]
print(student["skills"][1])