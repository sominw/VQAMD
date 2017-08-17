from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from random import shuffle
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
from sklearn.preprocessing import LabelEncoder
from spacy.en import English
from utils import group_together, freq_answers, ques_mat, ans_mat, img_mat

def main():

    training_questions = open("../preprocessed/ques_train.txt","rb").read().decode('utf8').splitlines()
    answers_train = open("../data/preprocessed/answer_train.txt","rb").read().decode('utf8').splitlines()
    images_train = open()
