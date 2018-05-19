# 3D Object Detection

This repository is to take SUNRGB-D 3D Object Detection Challenge with SegNet.

## Dependencies
- [NumPy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
- [Tensorflow](https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html)
- [Keras](https://keras.io/#installation)
- [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/)

## Dataset

Follow the [instruction](http://rgbd.cs.princeton.edu/challenge.html) to download dataset.

```bash
$ kaggle competitions download -c cvpr-2018-autonomous-driving -p /mnt/data
```

## Architecture

![image](https://github.com/foamliu/SegNet/raw/master/images/segnet.jpg)


## ImageNet Pretrained Models
Download [VGG16](https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels.h5) into models folder.

## Usage
### Data Pre-processing
Extract training images:
```bash
$ python pre-process.py
```

### Train
```bash
$ python train_depth.py
```

If you want to visualize during training, run in your terminal:
```bash
$ tensorboard --logdir path_to_current_dir/logs
```

### Demo

```bash
$ python demo_depth.py
```

Input | GT | Output |
|---|---|---|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/0_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/0_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/0_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/1_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/1_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/1_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/2_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/2_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/2_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/3_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/3_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/3_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/4_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/4_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/4_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/5_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/5_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/5_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/6_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/6_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/6_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/7_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/7_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/7_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/8_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/8_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/8_depth_label.png)|
|![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/9_depth_image.png)  | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/9_depth_label.png) | ![image](https://github.com/foamliu/3D-Object-Detection/raw/master/images/9_depth_label.png)|
