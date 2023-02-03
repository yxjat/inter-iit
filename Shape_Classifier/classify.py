from Main.classifier import shapeclassifier
import imutils
import cv2


#Image preprocessing:
image=cv2.imread("images3.jpg") #replace this with the path to file
resize=imutils.resize(image, width=300)
ratio=image.shape[0]/float(resize.shape[0])
# gray=cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
# blur=cv2.GaussianBlur(gray, (3,3), 0)
# thresh=cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY) [1]

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thres1.jpg', thresh)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blurred, 10, 100)

# define a (3, 3) structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# apply the dilation operation to the edged image
dilate = cv2.dilate(edged, kernel, iterations=1)

# find the contours in the dilated image
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_copy = image.copy()
# draw the contours on a copy of the original image
cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
print(len(contours), "objects were found in this image.")

cv2.imshow("Dilated image", dilate)
cv2.imshow("contours", image_copy)
cv2.waitKey(0)


# contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                      
# # draw contours on the original image
# image_copy = image.copy()
# cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
# # see the results
# cv2.imshow('None approximation', image_copy)
# cv2.waitKey(0)
# cv2.imwrite('contours_none_image1.jpg', image_copy)
# cv2.destroyAllWindows()


# contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # draw contours on the original image for `CHAIN_APPROX_SIMPLE`
# image_copy1 = image.copy()
# cv2.drawContours(image_copy1, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)
# # see the results
# cv2.imshow('Simple approximation', image_copy1)
# cv2.waitKey(0)
# cv2.imwrite('contours_simple_image1.jpg', image_copy1)
# cv2.destroyAllWindows()



#Contouring and initialising shapeclassifier:
# contour=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contour=imutils.grab_contours(contour)
sclass= shapeclassifier()

print(len(contours))
# Identifying contours:
for cnt in contours:
    M=cv2.moments(cnt)
    try:
        cntX = int((M["m10"] / M["m00"]) * ratio)
        cntY = int((M["m01"] / M["m00"]) * ratio)
    except:
        pass
    shape=sclass.classify(cnt)
    print(shape)
    cnt=cnt.astype("float")
    cnt*=ratio
    cnt=cnt.astype("int")
    cv2.drawContours(image, [cnt], -1, (0, 255, 0),2)

    cv2.imshow("Processed Img: ", image)
    cv2.waitKey(0)



