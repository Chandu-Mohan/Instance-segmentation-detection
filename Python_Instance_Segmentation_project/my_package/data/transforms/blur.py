#Imports
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''


    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur

        '''

        self.radius=radius
        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''



        image = image.filter(ImageFilter.GaussianBlur(self.radius))
        return image

'''
obj=BlurImage(5)
obj.__call__("/Users/buddamohanchandu/Desktop/Assignment-3/CS29006_SW_Lab_Spr2022/Python_DS_Assignment/data/imgs/7.jpg")

'''
