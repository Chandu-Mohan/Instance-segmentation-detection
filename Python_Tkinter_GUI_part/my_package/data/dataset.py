# Imports
import json
from PIL import Image
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms = transforms
        self.input=[]
        with open(annotation_file) as f:
            for line in f.readlines():
                self.input.append(json.loads(line))

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.input)

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        '''
        inp=Image.open('./data/' + self.input[idx]['img_fn'])

        if self.transforms is not None:
            for x in self.transforms:
                inp = x(inp)

        img_array = np.asarray(inp).transpose((2, 0, 1)) / 255
        annotations=[]
        for x in self.input[idx]['bboxes']:
            annotations.append([x['category']] + x['bbox'])

        return  {'image': img_array, 'gt_bboxes': annotations}

