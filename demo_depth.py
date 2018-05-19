# import the necessary packages
import cv2 as cv
import numpy as np
import keras.backend as K
import os
import random
from depth_model import build_encoder_decoder
from data_generator_depth import random_choice, safe_crop


if __name__ == '__main__':
    img_rows, img_cols = 320, 320
    channel = 3

    model_weights_path = 'models/depth_model.11-0.0114.hdf5'
    model = build_encoder_decoder()
    model.load_weights(model_weights_path)

    print(model.summary())

    rgb_test_path = 'data/rgb_test/'
    label_test_path = 'data/depth_test/'
    test_images = [f for f in os.listdir(rgb_test_path) if
                   os.path.isfile(os.path.join(rgb_test_path, f)) and f.endswith('.png')]

    samples = random.sample(test_images, 10)

    for i in range(len(samples)):
        image_name = samples[i]
        filename = os.path.join(rgb_test_path, image_name)
        label_path = os.path.join(label_test_path, image_name)
        image = cv.imread(filename)
        label = cv.imread(label_path)
        image_size = image.shape[:2]
        different_sizes = [(320, 320), (480, 480), (640, 640)]
        crop_size = random.choice(different_sizes)

        x, y = random_choice(image_size, crop_size)
        image = safe_crop(image, x, y, crop_size)
        label = safe_crop(label, x, y, crop_size)
        print('Start processing image: {}'.format(filename))

        x_test = np.empty((1, img_rows, img_cols, 3), dtype=np.float32)
        x_test[0, :, :, 0:3] = image / 255.

        out = model.predict(x_test)
        # print(out.shape)

        out = np.reshape(out, (img_rows, img_cols))
        out = out * 255.0
        out = out.astype(np.uint8)

        cv.imwrite('images/{}_depth_image.png'.format(i), image)
        cv.imwrite('images/{}_depth_out.png'.format(i), out)
        cv.imwrite('images/{}_depth_label.png'.format(i), label)

    K.clear_session()
