import cv2

img=cv2.imread("solar-system.jpg")

text_to_show = "sun"
cv2.putText(img, text_to_show, (5,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "mercury"
cv2.putText(img, text_to_show, (70,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "venus"
cv2.putText(img, text_to_show, (190,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "earth"
cv2.putText(img, text_to_show, (290,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "mars"
cv2.putText(img, text_to_show, (390,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "jupiter"
cv2.putText(img, text_to_show, (500,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "saturn"
cv2.putText(img, text_to_show, (750,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "uranus"
cv2.putText(img, text_to_show, (950,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))

text_to_show = "neptune"
cv2.putText(img, text_to_show, (1100,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(245,235,255))


cv2.imshow("output", img)

cv2.waitKey(5000)








