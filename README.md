# SVHN-Detection

In this homework, I apply [Yolov5](https://github.com/ultralytics/yolov5) on the assignment [2021 VRDL HW2](https://competitions.codalab.org/competitions/35888?secret_key=7e3231e6-358b-4f06-a528-0e3c8f9e328e#results)


## Installation

```
pip install -r requirements.txt
```

## Testing
#### 1. Download the trained weights 
Get my trained model from [here](https://drive.google.com/file/d/18n7ma7Fxx_CtarzpzTDfWfNesJbptY0G/view?usp=sharing) and put it in root directory

#### 2. Inference
``` 
python detect.py --weight best.pt --source data/svhn/test --device 0
```
The `answer.json` will be generated in `/runs/detect/exp/`

#### 3. Benchmark the derection model

Check the result in [inference.ipynb](https://drive.google.com/file/d/126rWkFlOuMcd9dOD_iplUJ8hjh-K5_cZ/view?usp=sharing)

## Prepare data

#### 1. Generate corresponding bounding box information for each image.
``` 
%cd data
python mat_to_yolo.py
```


#### 2. Split train dataset into train and valid manually

Move `*.png` from `/train/images` to `/valid/images` and `*.txt` from `train/labels` to `/valid/labels`

> Note that the two directory under `train` and `valid` must be `images` and `labels` because the training code recognizes them to pair each image and its txt file.

```
data
  | - mat_to_yolo.py
      ...
  | - svhn
      | - test
          | - 117.png 
              ...
      | - train
          | - images
              | - 1.png
                  ...
          | - labels
              | - 1.txt
                  ...
      | - valid
          | - images
              | - 30063.png
                  ...
          | - labels
              | - 30063.txt
                  ...
  
```

## Training

```
python train.py --img 320 --batch 64 --epochs 50 --weight yolov5l.pt --device 0
```
Pretrained weights are auto-downloaded in this code, you can also download it from [here](https://github.com/ultralytics/yolov5/releases).
I use `yolov5l` to get my final result.


## Reference

1. YOLOv5 - [Github](https://github.com/ultralytics/yolov5)
2. YOLO format data pre-process - [Street-View-House-Numbers-Detection](https://github.com/chia56028/Street-View-House-Numbers-Detection)

