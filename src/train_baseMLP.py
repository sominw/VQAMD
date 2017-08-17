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

    training_questions = open("../preprocessed/ques_train.txt","rb").read().decode('utf8').splitlines()
    answers_train = open("../data/preprocessed/answer_train.txt","rb").read().decode('utf8').splitlines()
    images_train = open("../data/preprocessed/images_coco_id.txt","rb").read().decode('utf8').splitlines()
    vgg_path = "/Users/sominwadhwa/Work/Minor/data/coco/vgg_feats.mat"
    upper_lim = 1500 #Number of most frequently occurring answers in COCOVQA (80%+)
    training_questions, answers_train, images_train = freq_answers(training_questions, answers_train, images_train, upper_lim)

    print (shape(training_questions), shape(answers_train), shape(images_train))
