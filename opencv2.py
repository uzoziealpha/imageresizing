# Write a script that resizes all images in a directory to 100x100. You can find an attached ZIP file with some image files in the Resources.

import cv2
#globe finds path names in a file with certain patterns
import glob



images=glob.glob("*.jpg")

#for loop to solve the exercise
for image in images:
    # the color os set to gray
    img=cv2.imread(image,0)
    # the dimensions are set and saved
    re=cv2.resize(img,(100,100))

    cv2.imshow("Hey",re)
    # the images will wait after 5 miliseconds = 5seconds
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # re holds the resized images 
    cv2.imwrite("resized_"+image,re)


# first created a list containing the image file paths and then iterated through the aforementioned list.
#The loop: reads each image, resizes, displays the image, waits for the user input key, 
# closes the window once the key is pressed, and writes the resized image. The name of the resized image will be "resized" plus the existing file name of the original image. 



