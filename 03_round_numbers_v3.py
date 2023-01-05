# https://from-locals.com/python-round-decimal-quantize/
def round_ans(val):
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


test_cases = [0.5, 0.2, 1.9, 0.51]
for item in test_cases:
    rounded = round_ans(item)
    print("{} is rounded to {}".format(item, rounded))
