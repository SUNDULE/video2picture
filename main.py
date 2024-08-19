import cv2
import os

path = 'video'

videoCapture = cv2.VideoCapture()
videoCapture.open('./video/00016.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

print("fps=", fps,"frames=",frames)

video_list = os.listdir(path)

for video in video_list:
    video_path = os.path.join(os.getcwd(),path,video)
    vc = cv2.VideoCapture(video_path)

    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
        cv2.imwrite(f'./picture/{video}_{c}.jpg', frame)
        print(c)
        c = c + 1
    else:
        rval = False

    while True:
        rval, frame = vc.read()
        if not rval:
            break

        cv2.imwrite(f'./picture/555_000{c}.jpg', frame)
        print(c)
        c = c + 1

    vc.release()
