import cv2

img=cv2.imread("C:/Users/asus/Desktop/Sample Picture/Google Translate2.png")
img2=cv2.Canny(img,127,255)
cv2.imshow("Edge Detection",img2)
cv2.imwrite("C:/Users/asus/Desktop/Google_Translate.png",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()