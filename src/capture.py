import cv2

capture = cv2.VideoCapture(0, cv2.CAP_ANY)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

time = 0    

if not capture.isOpened():
    print("WebCam is not running")
    exit()
    
while True:
    ret, frame = capture.read()
    time = time + 1
    cv2.imshow("VideoFrame", frame)
    
    if time == 100:
        cv2.imwrite('/home/computer520/Documents/opencv_study/capture/cap.png', frame) #-- 본인 편의에 맞게 경로 설정 및 이미지 이름 변경
        time = 0
    
    if cv2.waitKey(10) == 27:
        break
    
capture.release()
# captured.release()
cv2.destroyAllWindows()
