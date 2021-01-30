import cv2 



CAM_ADRESSES = [
    "/dev/video0",
    "/dev/video1",
    "/dev/video2"
]

camera = cv2.VideoCapture(CAM_ADRESSES[1])

while True:
    response ,frame = camera.read()
    if response:
        cv2.imshow("Frame", frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


camera.release()
cv2.destroyAllWindows()
