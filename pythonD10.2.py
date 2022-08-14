#function with multiple output
def format_name(fname,lname):
    if(fname=="" or lname==""):
        return "You didn't provide any input."
    formated_fname = fname.title()
    formated_lname = lname.title()
    return f"{formated_fname} {formated_lname}"
print(format_name(input("What is your first name? :"),input("What is your last name? :")))