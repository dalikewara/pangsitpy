import os
from pangsitpy.image_extraction import extract_to_array

source_file = os.path.join(os.path.dirname(__file__), 'files/image.png')
image_array = extract_to_array(source_file)
print(image_array)
print('=====')
image_array = extract_to_array(source_file, resize=True, array_to_int=True,
                               grayscale=True)
print(image_array)