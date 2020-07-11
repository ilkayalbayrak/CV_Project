import os
from glob import glob
import random

''' "Face dataset" has more than 90000 images, "masked face" dataset has around 2000 
     - Randomly remove images from face dataset to balance the sample sizes
         - Also shortens the training time a lot

'''

def remove_images(dataset_dir, number_to_remove=0):

    # Search for different file extensions, and concatenate the results
    image_extensions = ['**/*.jpg', '**/*.png']
    image_paths = glob(os.path.join(dataset_dir, image_extensions[0]), recursive = True) + glob(os.path.join(dataset_dir, image_extensions[1]), recursive = True)
    print('\nGiven dir contains: {} images'.format(len(image_paths)))

    # Number of images to remove from the dataset
    print('\n{} images will be removed from the dataset'.format(number_to_remove))

    for num in random.sample(range(len(image_paths)), number_to_remove ):
        os.remove(image_paths[num])
        removed_image_counter += 1

    print('\n{} images have been removed from the dataset'.format(removed_image_counter))
    print('finale')

# dataset_dir= 'self-built-masked-face-recognition-dataset/AFDB_face_dataset'
