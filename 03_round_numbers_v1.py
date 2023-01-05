def round_ans(to_round):
    to_round = round(to_round)
    return to_round


test_cases = [0.5, 0.2, 1.9, 0.51]
for item in test_cases:
    rounded = round_ans(item)
    print("{} is rounded to {}".format(item, rounded))
