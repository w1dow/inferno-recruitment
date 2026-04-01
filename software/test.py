import cv2

# Start
#   ↓
# Read Image
#   ↓
# Convert to Grayscale
#   ↓
# Detect Square Candidates (contours)
#   ↓
# Filter valid squares
#   ↓
# Apply Perspective Transform (make square)
#   ↓
# Convert to Black & White (threshold)
#   ↓
# Divide into Grid (4x4 / 5x5 / etc.)
#   ↓
# Extract Binary Pattern
#   ↓
# Check 4 Rotations
#   ↓
# Compare with Dictionary Patterns
#   ↓
# Match Found?
#    ↓           ↓
#   Yes          No
#    ↓            ↓
# Get ID        Reject Marker
#    ↓
# Return ID + Corners
#    ↓
# Draw Marker (optional)
#    ↓
# End



# img = cv2.imread("output.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# found = False

# for i in range(0,16) :
#     aruco_dict = cv2.aruco.getPredefinedDictionary(i)
#     detector = cv2.aruco.ArucoDetector(aruco_dict)

#     corners, ids, _ = detector.detectMarkers(gray)

#     if ids is not None:
#         print(i)
#         output = img.copy()
#         cv2.aruco.drawDetectedMarkers(output, corners, ids)

     
#         cv2.imshow(f"Detected", output)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

#         found = True
#         break 

# if not found:
#     print("No ArUco markers detected.")