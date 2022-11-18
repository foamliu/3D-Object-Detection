# -*- coding: utf-8 -*-

import os
import shutil
import tarfile

if __name__ == '__main__':

    if not os.path.exists('data/rgb'):
        os.makedirs('data/rgb')
    area_nos = [1, 2, 3, 4, 6]
    for area_no in area_nos:
        tar_file = 'area_{}_no_xyz.tar'.format(area_no)
        filename = os.path.join('data', tar_file)
        print('Extracting {}...'.format(filename))

        with tarfile.open(filename) as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar)

        folder = 'area_{}'.format(area_no)

        for f in [f for f in os.listdir(os.path.join(folder, 'data/rgb')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/rgb')
            src_path = os.path.join(src_path, f)
            dst_path = 'data/rgb/'
            shutil.move(src_path, dst_path)

        if not os.path.exists('data/depth'):
            os.makedirs('data/depth')
        for f in [f for f in os.listdir(os.path.join(folder, 'data/depth')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/depth')
            src_path = os.path.join(src_path, f)
            dst_path = 'data/depth/'
            shutil.move(src_path, dst_path)

        if not os.path.exists('data/semantic'):
            os.makedirs('data/semantic')
        for f in [f for f in os.listdir(os.path.join(folder, 'data/semantic_pretty')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/semantic_pretty')
            src_path = os.path.join(src_path, f)
            dst_path = 'data/semantic/'
            shutil.move(src_path, dst_path)

        shutil.rmtree(folder)

    if not os.path.exists('data/rgb_test'):
        os.makedirs('data/rgb_test')
    area_nos = ['5a', '5b']
    for area_no in area_nos:
        tar_file = 'area_{}_no_xyz.tar'.format(area_no)
        filename = os.path.join('data', tar_file)
        print('Extracting {}...'.format(filename))

        with tarfile.open(filename) as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar)

        folder = 'area_{}'.format(area_no)
        if not os.path.exists('data/rgb_test'):
            os.makedirs('data/rgb_test')
        for f in [f for f in os.listdir(os.path.join(folder, 'data/rgb')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/rgb')
            src_path = os.path.join(src_path, f)
            dst_path = 'data/rgb_test/'
            shutil.move(src_path, dst_path)

        if not os.path.exists('data/depth_test'):
            os.makedirs('data/depth_test')
        for f in [f for f in os.listdir(os.path.join(folder, 'data/depth')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/depth')
            src_path = os.path.join(src_path, f)
            dst_path = 'data/depth_test/'
            shutil.move(src_path, dst_path)

        if not os.path.exists('data/semantic_test'):
            os.makedirs('data/semantic_test')
        for f in [f for f in os.listdir(os.path.join(folder, 'data/semantic_pretty')) if f.endswith('.png')]:
            src_path = os.path.join(folder, 'data/semantic_pretty')
            src_path = os.path.join(src_path, f)
            dst_path = 'data/semantic_test/'
            shutil.move(src_path, dst_path)

    image_names = [f for f in os.listdir('data/rgb') if f.endswith('.png')]
    print('{} images'.format(len(image_names)))
    depth_names = [f for f in os.listdir('data/depth') if f.endswith('.png')]
    print('{} depths'.format(len(depth_names)))
    semantic_names = [f for f in os.listdir('data/semantic') if f.endswith('.png')]
    print('{} semantics'.format(len(semantic_names)))

    image_names = [f for f in os.listdir('data/rgb_test') if f.endswith('.png')]
    print('{} test images'.format(len(image_names)))
    depth_names = [f for f in os.listdir('data/depth_test') if f.endswith('.png')]
    print('{} test depths'.format(len(depth_names)))
    semantic_names = [f for f in os.listdir('data/semantic_test') if f.endswith('.png')]
    print('{} test semantics'.format(len(semantic_names)))
