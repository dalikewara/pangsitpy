import numpy as np
from PIL import Image
from skimage.io import imread, imsave
from skimage.transform import resize as imresize


def combine_and_save(source_files, output_file, arrangement='horizontal'):
    images = [Image.open(x) for x in source_files]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    if arrangement == 'vertical':
        new_im = Image.new('RGB', (max_height, total_width))
    else:
        new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        if arrangement == 'vertical':
            new_im.paste(im, (0, x_offset))
        else:
            new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    new_im.save(output_file)


def resize_and_save(source_file, output_file, target_size=(64, 64), grayscale=False):
    img = imread(source_file, as_gray=grayscale)
    img = imresize(img, target_size, anti_aliasing=True)
    img = 255 * img
    img = img.astype(np.uint8)
    imsave(output_file, img)
