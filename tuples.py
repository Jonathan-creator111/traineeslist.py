x=(10,20,30,40)
print(type(x))
print(x[3])
#convert to a list
x=list(x)
print(type(x))
x.append(100)
print(x)
#convert back to tuple
x=tuple(x)
print(x)
#Quiz
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
print(type(days))
days[3]="Thur"
print(days)
days=tuple(days)
print(type(days))