import cv2

class webcam:
    def __init__(self, src=0, width=640, height=480, fps=30.0, vid_name = 'output.avi'):
        self.cap = cv2.VideoCapture(src)
        self.fps = self.cap.set(cv2.CAP_PROP_FPS, fps)
        self.width = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.height = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.saved_vid = cv2.VideoWriter(vid_name, self.fourcc, fps, (width,  height))
        
        
    def show_webcam(self):
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
            
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
        
        
        
    def save_video(self):
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
            
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            self.saved_vid.write(frame)            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        # When everything done, release the capture
        self.cap.release()
        self.saved_vid.release()
        cv2.destroyAllWindows()