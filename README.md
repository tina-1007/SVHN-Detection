# SVHN-Detection

In this homework, I apply [Yolov5](https://github.com/ultralytics/yolov5) on the assignment [2021 VRDL HW2](https://competitions.codalab.org/competitions/35888?secret_key=7e3231e6-358b-4f06-a528-0e3c8f9e328e#results)


## Installation

```
pip install -r requirements.txt
```

## Testing
#### 1. Download the trained weights 
Get my trained model from [here](https://drive.google.com/file/d/1frwD4lEvk7e-xmWrdhHcMdLXeLVl31pU/view?usp=sharing) and put it in root directory

#### 2. Inference
``` 
python detect.py --weight best.pt --source data/svhn/test --device 0
```
The `answer.json` will be generated in `/runs/detect/exp/`

#### 3. Benchmark the derection model

Check the result in [inference.ipynb](https://drive.google.com/file/d/1KMKxUyQ12AiGK7cfw6d0esMJaFUFNyq3/view?usp=sharing)

## Prepare data

#### 1. Run `mat_to_yolo.py` in `/data`

To generate corresponding bounding box information for each image.
#### 2. Split train dataset into train and valid manually

Move xxx.png from `/train/images` to `/valid/images`
and `xxx.txt` from `train/labels` to `/valid/labels`

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
#### 1. Download official pre-trained yolo models
Get models in [this link](https://github.com/ultralytics/yolov5/releases/tag/v6.0), I use `yolov5m` to get my final result.

#### 2. Start training by running
```
python train.py --img 320 --batch 128 --epochs 50 --weight yolov5m.pt
```


## Reference

1. YOLOv5
    * [Github](https://github.com/ultralytics/yolov5)
2. YOLO format data pre-process 
    * [Street-View-House-Numbers-Detection](https://github.com/chia56028/Street-View-House-Numbers-Detection)

