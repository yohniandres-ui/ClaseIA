import cv2
import numpy as np

img_obj = cv2.imread("dragon.pnp", 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img_obj, None)

cap = cv2.VideoCapture(0)

bf = cv2.BFMatcher(cv2.NORM_HAMMING)

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp2, des2 = orb.detectAndCompute(gray, None)

    if des2 is not None:

        matches = bf.knnMatch(des1, des2, k=2)

        good = []

        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append(m)

        if len(good) > 10:

            pts = []

            for m in good:
                x, y = kp2[m.trainIdx].pt
                pts.append([x, y])

            pts = np.array(pts)

            x_min = int(np.min(pts[:,0]))
            x_max = int(np.max(pts[:,0]))
            y_min = int(np.min(pts[:,1]))
            y_max = int(np.max(pts[:,1]))

            cv2.rectangle(frame,
                          (x_min, y_min),
                          (x_max, y_max),
                          (255,0,0),
                          3)

        img_matches = cv2.drawMatches(
            img_obj, kp1,
            frame, kp2,
            good[:20], None
        )

        cv2.imshow("Deteccion", img_matches)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()