import numpy as np
import unittest
import cv2 as cv
from data_generator import train_gen


class TestStringMethods(unittest.TestCase):

    def test_data_generator(self):
        iter = train_gen()
        batch_x, batch_y = next(iter)
        for i in range(len(batch_x)):
            x = batch_x[i]
            y = batch_y[i]
            x = (x * 255.).astype(np.uint8)
            y = (y * 255.).astype(np.uint8)
            cv.imwrite('temp/test_data_generator_x_{}.png'.format(i), x)
            cv.imwrite('temp/test_data_generator_y_{}.png'.format(i), y)


if __name__ == '__main__':
    unittest.main()
