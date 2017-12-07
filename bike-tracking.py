import numpy as np
import cv2
import libbgs

bgs = libbgs.DPMean() #

person_in = 0
person_out = 0

#
# Define gates vertex
#

#               X    Y      X    Y
rec_top_in = [(230, 264), (340, 265)]  # TOP - IN
rec_top_ou = [(341, 267), (450, 268)]  # TOP - OUT

rec_bot_in = [(315, 805), (350, 806)]  # BOTTOM - IN
rec_bot_ou = [(280, 853), (308, 855)]  # BOTTOM - OUT

rec_lef_in = [(189, 561), (192, 610)]  # LEFT - IN
rec_lef_ou = [(215, 513), (217, 560)]  # LEFT - OUT

rec_rig_in = [(535, 510), (536, 570)]  # RIGHT - IN 532
rec_rig_ou = [(531, 571), (531, 631)]  # RIGHT - OUT

#
# Define colors
#
red_color = (0, 255, 0)
green_color = (0, 0, 255)
purple_color = (148, 0, 211)

#
# Function that understand the gate which contains the point
#
def point_in_out(center, frame):
    global person_in
    global person_out

    if rec_top_in[0][0] <= center[0] <= rec_top_in[1][0] \
            and rec_top_in[0][1] <= center[1] <= rec_top_in[1][1]:  # TOP - IN
        person_in += 1
        cv2.rectangle(frame, rec_top_in[0], rec_top_in[1], purple_color, 1)  # TOP - IN

    elif rec_top_ou[0][0] <= center[0] <= rec_top_ou[1][0] \
            and rec_top_ou[0][1] <= center[1] <= rec_top_ou[1][1]:  # TOP - OUT
        person_out += 1
        cv2.rectangle(frame, rec_top_ou[0], rec_top_ou[1], purple_color, 1)  # TOP - OUT

    if rec_lef_in[0][0] <= center[0] <= rec_lef_in[1][0] \
            and rec_lef_in[0][1] <= center[1] <= rec_lef_in[1][1]:  # LEFT - IN
        person_in += 1
        cv2.rectangle(frame, rec_top_in[0], rec_top_in[1], purple_color, 1)  # LEFT - IN

    elif rec_lef_ou[0][0] <= center[0] <= rec_lef_ou[1][0] \
            and rec_lef_ou[0][1] <= center[1] <= rec_lef_ou[1][1]:  # LEFT - OUT
        person_out += 1
        cv2.rectangle(frame, rec_lef_ou[0], rec_lef_ou[1], purple_color, 1)  # LEFT - OUT

    if rec_bot_in[0][0] <= center[0] <= rec_bot_in[1][0] \
            and rec_bot_in[0][1] <= center[1] <= rec_bot_in[1][1]:  # BOTTOM - IN
        person_in += 1
        cv2.rectangle(frame, rec_bot_in[0], rec_bot_in[1], purple_color, 1)  # BOTTOM - IN

    elif rec_bot_ou[0][0] <= center[0] <= rec_bot_ou[1][0] \
            and rec_bot_ou[0][1] <= center[1] <= rec_bot_ou[1][1]:  # BOTTOM - OUT
        person_out += 1
        cv2.rectangle(frame, rec_bot_ou[0], rec_bot_ou[1], purple_color, 1)  # BOTTOM - OUT

    if rec_rig_in[0][0] <= center[0] <= rec_rig_in[1][0] \
            and rec_rig_in[0][1] <= center[1] <= rec_rig_in[1][1]:  # RIGHT - IN
        person_in += 1
        cv2.rectangle(frame, rec_rig_in[0], rec_rig_in[1], purple_color, 1)  # RIGHT - IN

    elif rec_rig_ou[0][0] <= center[0] <= rec_rig_ou[1][0] \
            and rec_rig_ou[0][1] <= center[1] <= rec_rig_ou[1][1]:  # RIGHT - OUT
        person_out += 1
        cv2.rectangle(frame, rec_rig_ou[0], rec_rig_ou[1], purple_color, 1)  # RIGHT - OUT


if __name__ == "__main__":
    # Capture video
    cap = cv2.VideoCapture('video.mp4')
    
    # Defines Kernel matrix
    kernel_1 = np.ones((7, 7), np.uint8)
    kernel_2 = np.ones((10, 10), np.uint8)

    while 1:
        # Read frame from video
        ret, frame = cap.read()

        # Apply background subtraction
        fgmask = bgs.apply(frame)

        # Apply Opencv dilation
        fgmask = cv2.dilate(fgmask, kernel_1, iterations=3)
        
        # Apply Opencv closing
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel_2)

        # Apply threshold before find contours of moving object
        ret, thresh = cv2.threshold(fgmask, 127, 255, cv2.THRESH_TOZERO)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Display gates
        cv2.rectangle(frame, rec_top_in[0], rec_top_in[1], green_color, 1)  # TOP - IN
        cv2.rectangle(frame, rec_top_ou[0], rec_top_ou[1], red_color, 1)  # TOP - OUT

        cv2.rectangle(frame, rec_bot_in[0], rec_bot_in[1], green_color, 1)  # BOTTOM - IN
        cv2.rectangle(frame, rec_bot_ou[0], rec_bot_ou[1], red_color, 1)  # BOTTOM - OUT

        cv2.rectangle(frame, rec_lef_in[0], rec_lef_in[1], green_color, 1)  # LEFT - IN
        cv2.rectangle(frame, rec_lef_ou[0], rec_lef_ou[1], red_color, 1)  # LEFT - OUT

        cv2.rectangle(frame, rec_rig_in[0], rec_rig_in[1], green_color, 1)  # RIGHT - IN
        cv2.rectangle(frame, rec_rig_ou[0], rec_rig_ou[1], red_color, 1)  # RIGHT - OUT

        # Display Person in and out the roundabout
        cv2.putText(frame, "Person IN: " + str(person_in), (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, 2)

        cv2.putText(frame, "Person OUT: " + str(person_out), (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, 2)

        # cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
        if len(contours) > 1:
            for cnt in contours:
                if 1 < cv2.contourArea(cnt) < 850:
                    (x, y), radius = cv2.minEnclosingCircle(cnt)
                    center = (int(x), int(y))
                    radius = int(radius)
                    cv2.circle(frame, center, 1, green_color, 2)
                    cv2.circle(frame, center, radius, red_color, 2)
                    point_in_out(center, frame)
        
        # Show frame window
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', 600, 850)
        cv2.imshow('frame', frame)

        # Show background subtraction window
        #cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('frame2', 600, 850)
        #cv2.imshow('frame2', fgmask)

        # Halt on Esc key
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
