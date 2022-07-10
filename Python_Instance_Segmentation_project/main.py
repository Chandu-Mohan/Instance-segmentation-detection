#Imports

from my_package.model import InstanceSegmentationModel
from my_package.data.dataset import Dataset
from my_package.analysis.visualize import plot_visualization
from my_package.data.transforms import CropImage,RotateImage,FlipImage,BlurImage,RescaleImage

from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

def experiment(annotation_file, segmentor, transforms, output):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        segmentor: The image segmentor
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    data = Dataset(annotation_file, transforms)


    #Iterate over all data items.
    # Get the predictions from the segmentor.
    # Draw the segmentation maps on the image and save them.
    for i in range(len(data)):
        pred_boxes,pred_masks, pred_class, pred_score = segmentor(data[i]['image'])
        plot_visualization(data[i]['image'], pred_boxes,pred_masks, pred_class, output + f'/1/{i}.jpg')

    _, my_image_height, my_image_width = data[1]['image'].shape
    myanalysis = {'a': ('Original Image', []),
                  'b': ('Horizontally Flipped', [FlipImage()]),
                  'c': ('Blurred', [BlurImage(4)]),
                  'd': ('Twice Rescaled', [RescaleImage((2 * my_image_width, 2 * my_image_height))]),
                  'e': ('Half Rescaled', [RescaleImage((int(my_image_width / 2), int(my_image_height / 2)))]),
                  'f': ('90 Degree Right Rotated', [RotateImage(-90)]),
                  'g': ('45 Degree Left Rotated', [RotateImage(45)])}

    #Do the required analysis experiments.
    for ind, item in enumerate(myanalysis.items()):
        key, val = item
        data.transforms = val[1]
        pred_boxes,pred_masks, pred_class, pred_score = segmentor(data[7]['image'])
        plot_visualization(data[7]['image'], pred_boxes,pred_masks, pred_class, output + f'/2/{key}.jpg')
        plt.subplot(2, 4, ind + 1, title=val[0])
        plt.imshow(Image.open(output + f'/2/{key}.jpg'))

    plt.show()



def main():
    #imag = Image.open("/Users/buddamohanchandu/Desktop/Assignment-3/CS29006_SW_Lab_Spr2022/Python_DS_Assignment/data/imgs/9.jpg")
    #array= np.asarray(imag).transpose((2, 0, 1)) / 255

    segmentor = InstanceSegmentationModel()
    #pred_boxes, pred_masks, pred_class, pred_score = segmentor(array)
    #plot_visualization(array, pred_boxes, pred_masks, pred_class, pred_score)
    experiment('./data/annotations.jsonl', segmentor, None, '/Users/buddamohanchandu/Desktop/Assignment-3/CS29006_SW_Lab_Spr2022/Python_DS_Assignment/output') # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
