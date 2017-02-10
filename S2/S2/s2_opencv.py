import cv2

image = cv2.imread("tree.jpg")
cv2.imshow("main",image)
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
cv2.imshow("gray",grayimage)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('gray.jpg', grayimage)
    cv2.destroyAllWindows()

    