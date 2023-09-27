import cv2
import matplotlib.pyplot as plt

img = cv2.imread("faces.jpeg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# load the classifier
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
)

faces = face_detector.detectMultiScale(
    gray_img,
    scaleFactor=1.1,
    minNeighbors=11,
    minSize=(40,40)
)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(rgb_img)
plt.show()

