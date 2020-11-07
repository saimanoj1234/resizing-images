import cv2
img = cv2.imread('HappyFish.JPG', 1)
scale = 60 #1.for resizing images we do Downscale(Decrement in the size of the image) and Increment and resize either height or width and both
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dim = (width, height)

#2,for downscale take scale<100 and for increment take scale >100 i.e 400
print('Original Dimensions : ', img.shape) # (194, 259, 3)

#3.Resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape) #(116, 155, 3)

cv2.imshow("Resized image", resized)

m = cv2.waitKey(0)
if m == 63:
    cv2.destroyAllWindows()
elif m == ord('l'):
    cv2.imwrite("SadFish.jpg", img)
    cv2.destroyAllWindows()

