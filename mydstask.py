#Create a file called mydstask.py and attempt the below questions:
# my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
my_ds = "[23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]"
#1. Print KES
print(type(my_ds))
a=my_ds.find("KES")
print(a)
print(my_ds[55:57+1])
#2. Print 560
print(type(my_ds))
b=my_ds.find("560")
print(b)
print(my_ds[14:16+1])
#3. Print Maths
print(type(my_ds))
c=my_ds.find("Maths")
print(c)
print(my_ds[32:36+1])
#4. In the dictionary with the key currency, add another key “amount” with value 90
#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
    #Hint: Strings can be reversed using [::]
#6. Change the name “John” to “Jane” .
print(type(my_ds))
print(my_ds.replace("John","Jane"))