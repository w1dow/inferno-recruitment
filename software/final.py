import cv2
# link = "./test.mp4"
link = "http://10.150.119.99:8080/video"
cap = cv2.VideoCapture(link)
dict_id=[5]



    
if not cap.isOpened():
    print("Error opening camera")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("error in stream")
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for i in dict_id:
        dict=cv2.aruco.getPredefinedDictionary(i)
        detector = cv2.aruco.ArucoDetector(dict)
        corners, id, rejcted = detector.detectMarkers(gray)
        if id is not None:
            print(f"found aruco marker with id{id} and dict {i}")
            cv2.aruco.drawDetectedMarkers(frame,corners,id)
    # cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




# //works only for image
# img = cv2.imread("cmark.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# for i in range(22):
#     aruco_dict = cv2.aruco.getPredefinedDictionary(i)
#     detector = cv2.aruco.ArucoDetector(aruco_dict)

#     corners, ids, _ = detector.detectMarkers(gray)

#     if ids is not None:
#         cv2.aruco.drawDetectedMarkers(img, corners, ids)

# cv2.imshow("Output", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()