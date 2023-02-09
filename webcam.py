import cv2

def main():
    capture = cv2.VideoCapture(0)
    i = 0
    while(True):
        ret, frame = capture.read()
        frame = cv2.flip(frame,1)
        cv2.imshow("WEBCAM", frame)   
        k = cv2.waitKey(1)
        if k==32:
            i+=1
            cv2.imwrite(F'Caputura_{i}.png', frame)
        if k==27:
            break
    capture.release()
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()
