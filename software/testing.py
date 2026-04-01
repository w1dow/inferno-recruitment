# //works only for image
import cv2
dict_id=[8,9,10,11]
img = cv2.imread("image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for i in range(17):
    aruco_dict = cv2.aruco.getPredefinedDictionary(i)
    detector = cv2.aruco.ArucoDetector(aruco_dict)

    corners, id, rej = detector.detectMarkers(gray)

    if id is not None:
        print(f"found aruco marker with id{id} and dict {i}")
        cv2.aruco.drawDetectedMarkers(img, corners, id)
        
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()