import tensorflow 
import keras  
import os
import glob 
from skimage import io 
import random 
import numpy as np
import matplotlib.pyplot as plt

dataset_path = '/content/drive/MyDrive/Animals'
class_names = ['standing', 'mounted', 'mounting']

# apply glob module to retrieve files/pathnames  

image_path = os.path.join(dataset_path, class_names[1], '*')
image_path = glob.glob(image_path)

image = io.imread(animal_path[4])  

# plotting the original image
i, (im1) = plt.subplots(1)
i.set_figwidth(15)
im1.imshow(image)

i, (im1, im2, im3, im4) = plt.subplots(1, 4, sharey=True)
i.set_figwidth(20) 

im1.imshow(image)  #Original image
im2.imshow(image[:, : , 0]) #Red
im3.imshow(image[:, : , 1]) #Green
im4.imshow(image[:, : , 2]) #Blue
i.suptitle('Original & RGB image channels')

## Code to add data augmentation

