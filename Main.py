#introduction
print("Hello! Welcome to AloneTogether. I am the ChatBot.")
name = input("Please enter your name:")
age = int(input("Please enter your age:"))

#option
print("\n")
print("Hello", name, "how can I help you?")
print("[1] I am feeling ill")
print("[2] How do I prevent getting COVID-19?")
print("[3] I have other, general questions about COVID-19")
print("\n")

opt = int(input("Make a selection:"))

if opt==1:
    print("Would you like to see a list of symptoms?")
elif opt==2:
    print("Here are some things you can do:")
elif opt==3:
    print("What exactly would you like to know?")
else:
    print("invalid input")


