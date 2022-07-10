# Imports
from PIL import ImageDraw, Image, ImageFont
import numpy as np
import cv2
def colour(i,r,g,b):
    if(i%3==0):
        newr = r
        newg = 0
        newb = 0
        return newr, newg, newb
    if (i % 3 == 1):
        newr = 0
        newg = g
        newb = 0
        return newr, newg, newb
    if (i % 3 == 2):
        newr = 0
        newg = 0
        newb = b
        return newr, newg, newb

def plot_visualization(image, pred_boxes, pred_masks, pred_class,output):  # Write the required arguments

    # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
    # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
    image = Image.fromarray(np.uint8(image.transpose((1, 2, 0)) * 255))

    nob = min(len(pred_class), 3)
    for i in range(0,nob):

        ImageDraw.Draw(image).rectangle(pred_boxes[i], outline='blue', width=4)
        ImageDraw.Draw(image).text(pred_boxes[i][0], pred_class[i])

        d,h,w=pred_masks[i].shape
        print(pred_masks[i].shape)

        pixels = image.load()
        print((pred_masks[i])[0][1][1])
        print(pixels[1, 1])

        for py in range(h):
            for px in range(w):
                if ((pred_masks[i])[0][py][px] > 0.5 ):
                    r, g, b = pixels[px, py]

                    pixels[px, py] = colour(i,r,g,b)

    image.save(output)

