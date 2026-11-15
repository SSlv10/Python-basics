Name = str(input("Enter your name: "))
Age = int(input("Enter your age: "))

## To identify the data types
print(type(Age), type(Name))

if int(Age) >= 18:
    print("Hello, " + Name + "!" + " You are eligible to vote.")

else:
    print("Hello, " + Name + "!" + " You are not eligible to vote.")