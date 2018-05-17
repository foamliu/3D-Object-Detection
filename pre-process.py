# -*- coding: utf-8 -*-

import os
import shutil
import zipfile

if __name__ == '__main__':
    # if not os.path.exists('Combined_Dataset'):

    zip_files = ['train_color.zip', 'train_label.zip', 'train_video_list.zip', 'test.zip', 'test_video_list_and_name_mapping.zip', 'sample_submission.csv.zip']

    for zip_file in zip_files:
        filename = os.path.join('../../data', zip_file)
        print('Extracting {}...'.format(filename))

        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('.')
            zip_ref.close()
