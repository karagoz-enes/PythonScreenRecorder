import cv2
import pyautogui
import numpy as np

screen_size = pyautogui.size()
video = cv2.VideoWriter('Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'),18,screen_size)
print("recording...")
while True:
    screen_shot_img = pyautogui.screenshot()
    frame = np.array(screen_shot_img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video.write(frame)
    cv2.imshow("recording screen", frame)
    if cv2.waitKey == 29:
        break
cv2.destroyAllWindows()
video.release()

#neganwashere