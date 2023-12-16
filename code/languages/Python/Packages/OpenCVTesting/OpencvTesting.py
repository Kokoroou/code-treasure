import cv2 as cv
import os
# images = list(map(cv.imread, ["D:/test/test{}.jpg".format(i) for i in range(1,5)]))

# for n in range(len(images)):
# 	cv.imshow("Girl "+str(n), images[n])
# 	cv.waitKey()

# path = "D:/test/"
# cv.samples.addSamplesDataSearchPath(path)
# # img = cv.imread(cv.samples.findFile("Xiao_Yukiko.png"))
# img = cv.imread(cv.samples.findFile("test4.jpg"))
# cv.imshow("Xiao Yukiko", img)
# if (cv.waitKey() == ord("s")):
# 	cv.imwrite(path + "Xiao_Yukiko.png", img)

# file = open("cv_attributes.txt", mode="a+", encoding="utf-8")
# for i in cv.__dir__():
# 	file.write(i + "\n")
# file.close()
n = 1.5
img = cv.imread("test4.jpg", 1)
(h, w, d) = img.shape
rate = 624 / h
img = cv.resize(img, (int(w*rate), 624))

cv.imshow("first", img)
cv.waitKey(0)
print(img.shape)
print("Size of that photo is:\nheight = %d\nwidth = %d\ndepth = %d"%img.shape)

# img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("second", img1)
# cv.waitKey(0)


# cap = cv.VideoCapture("Món quà 20-10-2020.mp4")

# while(cap.isOpened()):	
# 	frame = cap.read()[1]
# 	cv.imshow("video", cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
# 	if cv.waitKey(40) == ord("q"): break

# cap.release()
# cv.destroyAllWindows()