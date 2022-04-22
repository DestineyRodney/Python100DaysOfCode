# Functions
# def my_function(something):
#     something = ""

def mult(num_1, num_2):
    result = num_1 * num_2
    return result


f_name = input("What is your first?").title()
l_name = input("What is your last name?").title()


def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    formated_f = first_name.title()
    formated_l = last_name.title()
    return f"{formated_f} {formated_l}"


print(format_name(first_name=f_name, last_name=l_name))



