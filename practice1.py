print("============= results =============== ")

x = int(input("enter the marks"))
if x>= 60:
    print("first class")
elif x>35 and x<=50:
    print("third class")
elif x>50 and x<=59:
    print("second class")
elif x==35:
    print("pass")
else:
    print("fails")

print("======================== practice with list =============================== ")
a = ["amer", "lokesh", "bashim","jishnu"," rakshid"]
for x in a :
    print(x)
print(a)
d = ["amer" ,"lokesh" , "bashim" ,"jishnu"  ," rakshid " ]
print(d)
for x in d:
    print(x)
for x in d:
    if str(x) and "a " in x:
        print(x)
for x in d:
        print(x)

print("============== if else ===============")

a = int(input("enter the value"))
b = int(input("enter the value"))
if a>b:
     print("a is greater")
else:
    print("b is greater")

print("======================= if elif else for driving licences ============================")

a = int(input("enter your age"))
if a>18 and a<59:
    print("you are eligible for licence" )
elif a == 60 :

    print("you had exceed the age limit ")
else:
  print("you are not eligible")

print("=========================nested if leap year example =============================")

years = int(input("enter the year"))
if years % 4 ==0:
    if years % 100 != 0:
        if years % 400 ==0:
            print("leep year")
        else:
            print ("nt leap year")
    else:
        print(" not leap yr")
else:
    print("not a leap year")

