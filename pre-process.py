# -*- coding: utf-8 -*-

import os
import shutil
import tarfile

if __name__ == '__main__':
    area_nos = [1, 2, 3, 4, 6]

    for area_no in area_nos:
        tar_file = 'area_{}_no_xyz.tar'.format(area_no)
        filename = os.path.join('data', tar_file)
        print('Extracting {}...'.format(filename))

        with tarfile.open(filename) as tar:
            tar.extractall()

        shutil.move('area_{}/data/rgb/*'.format(area_no), 'data/rgb/')
        shutil.move('area_{}/data/depth/*'.format(area_no), 'data/depth/')
        shutil.move('area_{}/data/semantic_pretty/*'.format(area_no), 'data/semantic/')

        shutil.rmtree('area_{}/'.format(area_no))

    image_names = [f for f in os.listdir('data/rgb') if f.endswith('.png')]
    print('{} images'.format(len(image_names)))
    depth_names = [f for f in os.listdir('data/depth') if f.endswith('.png')]
    print('{} depths'.format(len(depth_names)))
    semantic_names = [f for f in os.listdir('data/semantic') if f.endswith('.png')]
    print('{} semantics'.format(len(semantic_names)))
