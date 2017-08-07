import operator

def most_freq_answer(values):
    ans_dict = {}
    for index in range(10):
        ans_dict[values[index]['answer']] = 1
    for index in range(10):
        ans_dict[values[index]['answer']] += 1

    return max(ans_dict.items(), key = operator.itemgetter(1))[0]
