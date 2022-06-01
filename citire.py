import cv2 as cv

video = cv.VideoCapture('Videos/ping.mp4') 
nr_frameuri=count=0

while True:
    isTrue, frame =video.read()
    nr_frameuri+=1

    cv.imshow('Video',frame)
    if( nr_frameuri % 30 == 0): #din 30 in 30 de frameuri salvam unul
        cv.imwrite("Frameuri/frame%d.jpg" % count, frame)
        count += 1
        
    if cv.waitKey(20) & 0xFF==ord('x'): #daca se apasa x programul se opreste
        break
print("Frameuri: "  + str(nr_frameuri)) # numarul de frameuri parcurs pana la oprire

video.release()
cv.destroyAllWindows()


