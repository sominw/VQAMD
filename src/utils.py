import operator
from collections import defaultdict

def freq_answers(training_questions, answer_train, images_train, upper_lim):

    freq_ans = defaultdict(int)
    for ans in answer_train:
        freq_ans[ans] += 1

    sort_freq = sorted(freq_ans.items(), key=operator.itemgetter(1), reverse=True)[0:upper_lim]
    top_ans, top_freq = zip(*sort_freq)
    new_answers_train=[]
	new_questions_train=[]
	new_images_train=[]
    for ans,ques,img in zip(answers_train, training_questions, images_train):
		if ans in top_answers:
			new_answers_train.append(ans)
			new_questions_train.append(ques)
			new_images_train.append(img)
    return (new_questions_train,new_answers_train,new_images_train)


def most_freq_answer(values):
    ans_dict = {}
    for index in range(10):
        ans_dict[values[index]['answer']] = 1
    for index in range(10):
        ans_dict[values[index]['answer']] += 1

    return max(ans_dict.items(), key = operator.itemgetter(1))[0]
