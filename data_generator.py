import os
import random
from random import shuffle

import cv2 as cv
import numpy as np
from PIL import Image

from config import batch_size
from config import img_cols
from config import img_rows

train_color = '../../data/cvpr-2018-autonomous-driving/train_color'
train_label = '../../data/cvpr-2018-autonomous-driving/train_label'

class_dict = {0: 'others', 33: 'car', 34: 'motorbicycle', 35: 'bicycle', 36: 'person', 38: 'truck', 39: 'bus',
              40: 'tricycle'}
inv_dict = {v: k for k, v in class_dict.items()}
gray_scales = {'other': 0, 'person': 255, 'car': 224, 'bus': 192, 'truck': 160,
                   'motorbicycle': 128, 'bicycle': 96, 'tricycle': 64}


def get_label(name):
    label_name = name.split('.')[0] + '_instanceIds.png'
    filename = os.path.join(train_label, label_name)
    label = np.asarray(Image.open(filename)) // 1000
    for class_name in ['person', 'car', 'bus', 'truck', 'motorbicycle', 'bicycle', 'tricycle']:
        label[label == inv_dict[class_name]] = gray_scales[class_name]
    label[(label != 255) & (label != 224) & (label != 192) & (label != 160) & (label != 128) & (label != 96) & (label != 64)] = 0
    return label


# Randomly crop 320x320 (image, label) pairs centered on pixels in the known regions.
def random_choice(label):
    y_indices, x_indices = np.where(label != 0)
    num_knowns = len(y_indices)
    x, y = 0, 0
    if num_knowns > 0:
        ix = random.choice(range(num_knowns))
        center_x = x_indices[ix]
        center_y = y_indices[ix]
        x = max(0, center_x - 160)
        y = max(0, center_y - 160)
    return x, y


def safe_crop(mat, x, y):
    if len(mat.shape) == 2:
        ret = np.zeros((320, 320), np.float32)
    else:
        ret = np.zeros((320, 320, 3), np.float32)
    crop = mat[y:y + 320, x:x + 320]
    h, w = crop.shape[:2]
    ret[0:h, 0:w] = crop

    return ret


def data_gen(usage):
    filename = '{}_names.txt'.format(usage)
    with open(filename, 'r') as f:
        names = f.read().splitlines()
    i = 0
    while True:
        batch_x = np.empty((batch_size, img_rows, img_cols, 3), dtype=np.float32)
        batch_y = np.empty((batch_size, img_rows, img_cols, 1), dtype=np.float32)

        for i_batch in range(batch_size):
            print(i_batch)
            name = names[i]
            filename = os.path.join(train_color, name)
            image = cv.imread(filename)
            label = get_label(name)

            x, y = random_choice(label)
            image = safe_crop(image, x, y)
            label = safe_crop(label, x, y)

            if np.random.random_sample() > 0.5:
                image = np.fliplr(image)
                label = np.fliplr(label)

            batch_x[i_batch, :, :, 0:3] = image / 255.
            batch_y[i_batch, :, :, 0] = label / 255.

            i += 1
            if i >= len(names):
                i = 0

        yield batch_x, batch_y


def train_gen():
    return data_gen('train')


def valid_gen():
    return data_gen('valid')


def shuffle_data():
    num_samples = 39222
    num_train_samples = 31378
    num_valid_samples = 7844
    train_folder = '../../data/cvpr-2018-autonomous-driving/train_color'
    names = [f for f in os.listdir(train_folder) if f.endswith('.jpg')]
    valid_names = random.sample(names, num_valid_samples)
    train_names = [n for n in names if n not in valid_names]
    shuffle(valid_names)
    shuffle(train_names)

    with open('valid_names.txt', 'w') as file:
        file.write('\n'.join(valid_names))

    with open('train_names.txt', 'w') as file:
        file.write('\n'.join(train_names))


if __name__ == '__main__':
    shuffle_data()
