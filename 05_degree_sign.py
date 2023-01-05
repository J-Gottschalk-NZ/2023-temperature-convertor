# https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python
degree_sign = u'\N{DEGREE SIGN}'

test_cases = [2, 4, 23.2]

for item in test_cases:
    print("{}{}C".format(item, degree_sign))
