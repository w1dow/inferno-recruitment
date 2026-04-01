import cv2
img = cv2.imread("image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

found=False
ids=[]

for i in range(0,22) :
    aruco_dict = cv2.aruco.getPredefinedDictionary(i)
    detector = cv2.aruco.ArucoDetector(aruco_dict)

    corners, id, _ = detector.detectMarkers(gray)

    if id is not None:
        print(i)
        output = img.copy()
        ids.append(id)
        cv2.aruco.drawDetectedMarkers(output, corners, id)
        print(f"found aruco with id{id}")
        found=True

cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

if not found:
    print("No ArUco markers detected.")


# # //generating an aruco mrkr
# dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# output = cv2.aruco.generateImageMarker(dict,23,200);
# cv2.imshow("output",output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("output.png",output)