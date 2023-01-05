# https://from-locals.com/python-round-decimal-quantize/
def round_ans(val, digit=0):
    p = 10 ** digit
    var_rounded = (val * p * 2 + 1) // 2 / p
    return "{:.0f}".format(var_rounded)


test_cases = [0.5, 0.2, 1.9, 0.51]
for item in test_cases:
    rounded = round_ans(item)
    print("{} is rounded to {}".format(item, rounded))
