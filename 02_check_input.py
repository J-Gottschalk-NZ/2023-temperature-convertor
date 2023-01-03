def check_temp(min_value):
    error = "Please enter a number that is more " \
            "than {}".format(min_value)

    try:
        response = float(input("Choose a number: "))

        if response < min_value:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


# *** Main routine ****

while True:
    to_check = check_temp(-459)
    print("Success")
