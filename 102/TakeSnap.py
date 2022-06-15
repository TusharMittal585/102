import cv2

def takeSnapshot():
    videoCaptureObj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame=videoCaptureObj.read()
        cv2.imwrite('picture1.jpg',frame) 
        result=False
    
    videoCaptureObj.release()
    cv2.destroyAllWindows() 

takeSnapshot() 