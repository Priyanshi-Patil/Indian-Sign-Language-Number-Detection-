import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             '0': len(os.listdir(directory+"/0")),
             '1': len(os.listdir(directory+"/1")),
             '2': len(os.listdir(directory+"/2")),
             '3': len(os.listdir(directory+"/3")),
             '4': len(os.listdir(directory+"/4")),
             '5': len(os.listdir(directory+"/5")),
             '6': len(os.listdir(directory+"/6")),
             '7': len(os.listdir(directory+"/7")),
             '8': len(os.listdir(directory+"/8")),
             '9': len(os.listdir(directory+"/9")),
             }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['0'])+'.png',frame)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['1'])+'.png',frame)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['2'])+'.png',frame)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['3'])+'.png',frame)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['4'])+'.png',frame)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['5'])+'.png',frame)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['6'])+'.png',frame)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['7'])+'.png',frame)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['8'])+'.png',frame)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['9'])+'.png',frame)
cap.release()
cv2.destroyAllWindows()