#Imports
from PIL import Image


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.shape = shape

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here

        w, h = image.size
        left = int(w / 2 - (self.shape[1]) / 2)
        top = int(h / 2 - (self.shape[0]) / 2)
        right = int(w / 2 + (self.shape[1]) / 2)
        bottom = int(h / 2 + (self.shape[0]) / 2)
        image = image.crop((left, top, right, bottom))

        return image

