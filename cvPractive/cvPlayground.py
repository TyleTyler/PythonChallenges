import numpy as np
import cv2 as cv 

# cap =  cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('Display Window','frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()



# # Load two images
# img1 = cv.imread("cvPractive\otherShot.png")
# img2 = cv.imread('cvPractive\Screenshot_1.png')
# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"
# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols]
# cv.imshow('Display Window', roi)
# k = cv.waitKey(0)
# # Now create a mask of logo and create its inverse mask also
# img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# cv.imshow('Display Window',img2gray)
# k = cv.waitKey(0)

# ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
# cv.imshow('Display Window',mask)
# k = cv.waitKey(0)

# mask_inv = cv.bitwise_not(mask)
# cv.imshow('Display Window',mask_inv)
# k = cv.waitKey(0)

# # Now black-out the area of logo in ROI
# img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# cv.imshow('Display Window',img1_bg)
# k = cv.waitKey(0)

# # Take only region of logo from logo image.
# img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# cv.imshow('Display Window',img2_fg)
# k = cv.waitKey(0)

# # Put logo in ROI and modify the main image
# dst = cv.add(img1_bg,img2_fg)
# cv.imshow('Display Window', dst)

# img1[0:rows, 0:cols ] = dst
# cv.imshow('res',img1)
# cv.waitKey(0)


cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_green = np.array([36,25,25])
    upper_green = np.array([70,255,255])
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
      
      
    # Threshold the HSV image to get only blue colors
    gmask = cv.inRange(hsv, lower_green, upper_green)
    bmask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= bmask)
    res = cv.bitwise_and(frame,frame, mask= gmask)
    
    cv.imshow('frame',frame)
    cv.imshow('blue mask',bmask)
    cv.imshow('green mask',gmask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
# red = np.uint8([[[0,0,2]]])
# hsv_green = cv.cvtColor(red,cv.COLOR_BGR2HSV)
# print( hsv_green )