from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from random import shuffle
import numpy as np
import scipy.io
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
from sklearn.preprocessing import LabelEncoder
from spacy.en import English
from utils import freq_answers

def main():

    training_questions = open("../preprocessed/ques_train.txt","rb").read().splitlines()
    answers_train = open("../preprocessed/answer_train.txt","rb").read().splitlines()
    images_train = open("../preprocessed/images_coco_id.txt","rb").read().splitlines()
    img_ids = open('../preprocessed/coco_vgg_IDMap.txt').read().splitlines()
    vgg_path = "/Users/sominwadhwa/Work/Minor/data/coco/vgg_feats.mat"
    print (vgg_path)
    upper_lim = 1500 #Number of most frequently occurring answers in COCOVQA (85%+)
    training_questions, answers_train, images_train = freq_answers(training_questions, answers_train, images_train, upper_lim)
    print (len(training_questions), len(answers_train),len(images_train))
    num_hidden_units = 1024
    num_hidden_layers = 3
    batch_size = 128
    dropout = 0.5
    activation = tanh
    log_interval = 10


if __name__ == '__main__':
    main()
