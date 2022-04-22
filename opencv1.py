#open Cv allows the computer to read images
import cv2 

#reading the images in color with 1
#img=cv2.imread("Snowman.jpg", 1)

#reading the images in gray
img=cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)

#shape
print(img.shape)

#dimension
print(img.ndim)


#resizing the images with tuples
resized_image=cv2.resize(img,(1000,500))
cv2.imshow("Galaxy", resized_image)


#show the image window on the screen
#cv2.imshow("Galaxy", img)

# specify 0 to make the image stay with no time limits
cv2.waitKey(0)

#specify a time in = 2000 means miliseconds 2 seconds 
#cv2.waitKey(2000)


cv2.destroyAllWindows()