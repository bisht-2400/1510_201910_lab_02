#kshitiz bisht
#A01053490
#22-01-2019


def format_name():
    """Print after concatenating 2 strings
    PARAM a an string
    PARAM b an string
    PRE-CONDITION a must be a string
    PRE-CONDITION b must be a string
    RETURN concatenation of a and b"""
    first_name = input("Enter your first name: ")
    last_name = input("Enter the last name: ")
    first_strip = first_name.strip()
    last_strip = last_name.strip()
    first_title = first_strip.title()
    last_title = last_strip.title()
    full_name = first_title+" "+last_title
    print("Full name is", full_name)
    return full_name


def doubler():
    """print after doubling the input
    PARAM a is any int float or string
    RETURN double the input a"""
    inpt = input("ENTER: ")
    outpt = 2*inpt
    print(outpt)
    return inpt


def this_year():
    """Print the number 2018
    PARAM a is an int
    PARAM b is an int
    PRE-CONDITION a must be a int
    PRE-CONDITION b must be a int
    RETURN the sum of a and b"""
    first = int(input("enter your age: "))
    second = int(input("enter your year of birth"))
    print("current year=", first+second)

def base_converter():
        num = int(input("enter the number: "))
        base = int(input("enter the base to be converted to : "))
        q1 = num // base
        n1 = num % base
        converted_num = n1
        num = q1
        q1 = num // base
        n2 = num % base
        converted_num = converted_num + n2 * 10
        num = q1
        q1 = num // base
        n3 = num % base
        converted_num = converted_num + n3 * 100
        num = q1
        q1 = num // base
        n4 = num % base
        converted_num = converted_num + n4 * 1000
        print("converted number is: ", converted_num)


def main():
    format_name()
    doubler()
    this_year()
    base_converter()


if __name__ == '__main__':

    main()
