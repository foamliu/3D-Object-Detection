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

        folder = 'area_{}'.format(area_no)

        for f in [f for f in os.listdir(os.path.join(folder, 'data/rgb')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/rgb')
            src_path = os.path.join(src_path, f)
            dst_path = os.path.join('data/rgb/', f)
            shutil.move(src_path, dst_path)

        for f in [f for f in os.listdir(os.path.join(folder, 'data/depth')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/depth')
            src_path = os.path.join(src_path, f)
            dst_path = os.path.join('data/depth/', f)
            shutil.move(src_path, dst_path)

        for f in [f for f in os.listdir(os.path.join(folder, 'data/semantic_pretty')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/semantic_pretty')
            src_path = os.path.join(src_path, f)
            dst_path = os.path.join('data/semantic/', f)
            shutil.move(src_path, dst_path)

        shutil.rmtree(folder)

    image_names = [f for f in os.listdir('data/rgb') if f.endswith('.png')]
    print('{} images'.format(len(image_names)))
    depth_names = [f for f in os.listdir('data/depth') if f.endswith('.png')]
    print('{} depths'.format(len(depth_names)))
    semantic_names = [f for f in os.listdir('data/semantic') if f.endswith('.png')]
    print('{} semantics'.format(len(semantic_names)))
