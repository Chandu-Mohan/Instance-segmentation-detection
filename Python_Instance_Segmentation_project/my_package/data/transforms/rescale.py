# Imports
from PIL import Image


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here

        width, height = image.size
        if type(self.output_size) == tuple:
            new_size = (self.output_size[0], self.output_size[1])
            image = image.resize(new_size)
        else:
            if width > height:
                ratio = float(self.output_size) / height
                new_size = (int(width * ratio), self.output_size)
                image = image.resize(new_size)
            else:
                new_size = (width, self.output_size)
                image = image.resize(new_size)
        #image.show()
        return image

'''
f = 50
obj = RescaleImage(f)
obj.__call__("/Users/buddamohanchandu/Desktop/Assignment-3/CS29006_SW_Lab_Spr2022/Python_DS_Assignment/data/imgs/7.jpg")
'''
