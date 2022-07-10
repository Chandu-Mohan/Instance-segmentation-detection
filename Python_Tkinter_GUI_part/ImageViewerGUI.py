####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
from functools import partial

import numpy as np
import PIL.Image
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_visualization
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
from PIL import ImageTk

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import *
from tkinter import filedialog


# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):
    ####### CODE REQUIRED (START) #######
    global my_Image

    root.filename= filedialog.askopenfilename(initialdir="/Users/buddamohanchandu/Desktop/Assignment-4/Python_Tkinter_Assignment/data/imgs",title="images")
    inp = PIL.Image.open(root.filename)
    img_array = np.asarray(inp).transpose((2, 0, 1)) / 255
    pred_boxes,pred_masks, pred_class, pred_score = segmentor(img_array)
    plot_visualization(img_array, pred_boxes,pred_masks, pred_class,"/Users/buddamohanchandu/Desktop/Assignment-4/Python_Tkinter_Assignment/output/1.jpg","/Users/buddamohanchandu/Desktop/Assignment-4/Python_Tkinter_Assignment/output/2.jpg")
    # This function should pop-up a dialog for the user to select an input image file.
    # Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
    # Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
    # Once the output is computed it should be shown automatically based on choice the dropdown button is at.
    # To have a better clarity, please check out the sample video.
    return


####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def  process(clicked):
    ####### CODE REQUIRED (START) #######
    global my_Image
    try:
        root.filename
    except:
       print("No file selected!!!")
    else:
        if(clicked.get()=="Segmentation"):
            my_Image = ImageTk.PhotoImage(PIL.Image.open("/Users/buddamohanchandu/Desktop/Assignment-4/Python_Tkinter_Assignment/output/1.jpg"))
            my_Image_lable= Label(image=my_Image)
            my_Image_lable.grid(row=1,column=0)
        else:
            my_Image = ImageTk.PhotoImage(PIL.Image.open("/Users/buddamohanchandu/Desktop/Assignment-4/Python_Tkinter_Assignment/output/2.jpg"))
            my_Image_lable = Label(image=my_Image)
            my_Image_lable.grid(row=1, column=0)

    # Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
    # Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
    # Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
    return


####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':

    ####### CODE REQUIRED (START) ####### (2 lines)
    # Instantiate the root window.
    # Provide a title to the root window.
    root = Tk()
    root.title("--Image Viewer--")

    ####### CODE REQUIRED (END) #######

    # Setting up the segmentor model.
    annotation_file = './data/annotations.jsonl'
    transforms = []

    # Instantiate the segmentor model.
    segmentor = InstanceSegmentationModel()
    # Instantiate the dataset.
    dataset = Dataset(annotation_file, transforms=transforms)

    # Declare the options.
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])

    e = Entry(root, width=70)
    e.grid(row=0, column=0)

    ####### CODE REQUIRED (START) #######
    # Declare the file browsing button
    browseButton = Button(root, text="Browse",command=partial(fileClick,clicked, dataset, segmentor))
    browseButton.grid(row=0, column=1)
    ####### CODE REQUIRED (END) #######


	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
    ddown = OptionMenu(root, clicked, *options)
    ddown.grid(row=0, column=2)
    ####### CODE REQUIRED (END) #######

    # This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process", command=partial(process, clicked))
    myButton.grid(row=0, column=3)

    ####### CODE REQUIRED (START) ####### (1 line)
    # Execute with mainloop()
    root.mainloop()
    ####### CODE REQUIRED (END) #######
