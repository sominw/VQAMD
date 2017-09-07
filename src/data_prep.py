import json   #parse json
import argparse
import spacy  #tokenizing text
import progressbar
from utils import most_freq_answer

parser = argparse.ArgumentParser()
parser.add_argument('-split', type=str, default='train',
		help='Specify which part of the dataset you want to dump to text. Your options are: train, val')
args = parser.parse_args()

nlp = spacy.load("en")
print ("hello")
if args.split == "train":
    #Create all relevant data-dumps required
    image_set_id = open('../preprocessed/images_coco_id.txt','wb')
    ann = '../data/v2_mscoco_train2014_annotations.json'
    ques = '../data/v2_OpenEnded_mscoco_train2014_questions.json'
    ques_compile = open('../preprocessed/ques_train.txt', 'wb')
    ques_id = open('../preprocessed/ques_train_id.txt', 'wb')
    ques_len = open('../preprocessed/ques_train_len.txt', 'wb')
    answer_train = open('../preprocessed/answer_train.txt','wb')
    data_split = "training data"

elif args.split == "val":
    image_set_id = open('../preprocessed/images_coco_id_val.txt','wb')
    ann = '../data/v2_mscoco_val2014_annotations.json'
    ques = '../data/v2_OpenEnded_mscoco_val2014_questions.json'
    ques_compile = open('../preprocessed/ques_val.txt', 'wb')
    ques_id = open('../preprocessed/ques_val_id.txt', 'wb')
    ques_len = open('../preprocessed/ques_val_len.txt', 'wb')
    answer_train = open('../preprocessed/answer_val.txt','wb')
    data_split = "validation data"


ques = json.load(open(ques,'r'))
questions = ques['questions']
qa = json.load(open(ann,'r'))
annotations = qa['annotations']

progress = progressbar.ProgressBar()
print ("Begin Data Dump...")
for index, q in progress(zip(range(len(questions)),questions)):
    ques_compile.write((q['question'] + '\n').encode('utf8'))
    ques_len.write((str(len(nlp(q['question']))) + '\n').encode('utf8'))
    ques_id.write((str(q['question_id'])+'\n').encode('utf8'))
    image_set_id.write((str(q['image_id'])+'\n').encode('utf8'))
    answer_train.write(most_freq_answer(annotations[index]['answers']).encode('utf8'))
    answer_train.write('\n'.encode('utf8'))

print (data_split, "dumping completed")
print ("Data dump can be found in ../preprocessed/")
