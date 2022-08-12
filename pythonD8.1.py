#simple function
def greet():
    print("HELLO FRIEND")
    print("HOW ARE YOU?")
    print("GOOD BYE")
greet()
#funtions with parameters
def greet_with_name(name):
    print(f"hello {name}")
    print(f"good bye {name}")
greet_with_name("jack")
#fiunction with multiple parameters
def greet_with_multiple(name, location):
    print(f"HELLO {name}")
    print(f"What is it like in {location}")
#Call by positional arguements
greet_with_multiple("Jack","Jersey")
#Call by keyword arguements
greet_with_multiple(location="Jersey",name="Jack")
#Call by variables
location = "Jersey"
name = "Jack"
greet_with_multiple(location,name)
