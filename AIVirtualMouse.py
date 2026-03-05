import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
 
##########################
wCam, hCam = 640, 480
frameR = 100
smoothening = 7
##########################
 
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
leftCooldown = 0
rightCooldown = 0
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
 
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
 
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if not success:
        continue
 
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
 
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        xThumb, yThumb = lmList[4][1:]
 
        fingers = detector.fingersUp()
 
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)
 
        # ================= MOVE =================
        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
 
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
 
            autopy.mouse.move(clocX, clocY)
            cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)
 
            plocX, plocY = clocX, clocY
 
        # ================= LEFT CLICK =================
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 35 and time.time() - leftCooldown > 0.25:
                autopy.mouse.click(autopy.mouse.Button.LEFT)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                leftCooldown = time.time()
 
        # ================= RIGHT CLICK =================
        # Thumb + Index pinch (more reliable)
        length, img, lineInfo = detector.findDistance(4, 8, img)
        if length < 35 and fingers[2] == 0 and time.time() - rightCooldown > 0.25:
            autopy.mouse.click(autopy.mouse.Button.RIGHT)
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 18, (255, 0, 0), cv2.FILLED)
            rightCooldown = time.time()
 
    # FPS
    cTime = time.time()
    fps = 1/(cTime-pTime) if (cTime-pTime)!=0 else 0
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)
 
    cv2.imshow("AI Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
 
cap.release()
cv2.destroyAllWindows()