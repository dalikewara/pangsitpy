import re
import numpy as np
from skimage.io import imread
from skimage.transform import resize as imresize
from keras.preprocessing.image import load_img, img_to_array


def extract_to_array(source_file, target_size=(64, 64), engine='skimage',
                     grayscale=False, resize=False, labels=None,
                     array_to_int=False, types=None):
    filename = source_file.split('/')[::-1][0]
    img_label = 0
    img_type = 0
    img_prefix = 0
    if engine == 'skimage':
        img = imread(source_file, as_gray=grayscale)
        if resize == True:
            img = imresize(img, target_size, anti_aliasing=True)
        img = 255 * img
        if array_to_int == True:
            img = img.astype(np.uint8)
        img_array = img
        img_shape = img.shape
    else:
        if resize == True:
            img = load_img(source_file, target_size=target_size, grayscale=grayscale)
        else:
            img = load_img(source_file, grayscale=grayscale)
        img_array = img_to_array(img)
        img_shape = [img_array.shape[0], img_array.shape[1], img_array.shape[2]]
    try:
        img_shape = (img_shape[0], img_shape[1], img_shape[2])
    except:
        img_shape = (img_shape[0], img_shape[1], 1)
    if labels:
        for lbl in labels:
            if lbl[0] and (re.search('' + lbl[0], filename) != None):
                img_prefix = lbl[0]
                try:
                    img_label = lbl[1]
                except:
                    img_label = 0
    if types:
        for tp in types:
            if (tp[0] != '') and (re.search('' + tp[0], filename) != None):
                img_type = tp[0]
    return {
        "array": img_array,
        "shape": img_shape,
        "prefix": img_prefix,
        "label": img_label,
        "type": img_type
    }
