import h5py
import cv2
from tqdm import tqdm


def getName(data, n):
    digitStructName = data['digitStruct']['name'][n]
    return ''.join([chr(v[0]) for v in data[(digitStructName[0])]])


def getBbox(data, n):
    bbox = {}
    bb = data['digitStruct']['bbox'][n].item()
    bbox['height'] = bboxHelper(data[bb]["height"])
    bbox['left'] = bboxHelper(data[bb]["left"])
    bbox['top'] = bboxHelper(data[bb]["top"])
    bbox['width'] = bboxHelper(data[bb]["width"])
    bbox['label'] = bboxHelper(data[bb]["label"])

    return bbox


def bboxHelper(attr):
    if len(attr) > 1:
        attr = [data[attr[j].item()][0][0] for j in range(len(attr))]
    else:
        attr = [attr[0][0]]
    return attr

if __name__ == "__main__":
    dir_path = './data/svhn/train/'  # path to train directory
    img_path = dir_path + 'images/'
    file_path = dir_path + 'digitStruct.mat'

    data = h5py.File(file_path, 'r')
    digitStructName = data['digitStruct']['name']
    digitStructBbox = data['digitStruct']['bbox']

    data_len = len(digitStructName)
    print('There are {} training images.'.format(data_len))

    for i in tqdm(range(data_len)):
        img_name = getName(data, i)
        bboxes = getBbox(data, i)
        im = cv2.imread(img_path + img_name)
        h, w, c = im.shape

        fp = open(dir_path + 'labels/' + img_name.replace('.png', '.txt'), 'w')
        b_num = len(bboxes['label'])
        for idx in range(b_num):
            label = int(bboxes['label'][idx] % 10)
            _l = bboxes['left'][idx]
            _t = bboxes['top'][idx]
            _w = bboxes['width'][idx]
            if (_l + _w) > w:
                _w = w - _l - 1
            _h = bboxes['height'][idx]
            if (_t + _h) > h:
                _h = h - _t - 1
            # print(w, h, _l, _t, _w , _h)
            x_center = (_l + _w/2)/w
            y_center = (_t + _h/2)/h
            bbox_width = _w/w
            bbox_height = _h/h
            # print(label, x_center, y_center, bbox_width, bbox_height)
            s = "{} {} {} {} {}".format(str(label),
                                        str(x_center),
                                        str(y_center),
                                        str(bbox_width),
                                        str(bbox_height))
            if idx != (b_num - 1):
                s += '\n'
            fp.write(s)
        fp.close()
