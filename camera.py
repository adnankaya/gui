import cv2 as cv


class Camera:
    def __init__(self, *args, **kwargs):
        try:
            if not 'cam_source' in kwargs:
                self.camera = cv.VideoCapture(0, cv.CAP_V4L)
            else:
                cam_source = kwargs['cam_source']
                self.camera = cv.VideoCapture(cam_source, cv.CAP_V4L)
                if not self.camera.isOpened():
                    raise ValueError("Unable to open video source", cam_source)
        except Exception as exc:
            raise exc

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_origin_frames(self):
        '''returns received frame as BGR '''
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return frame

    def resize_frame(self, img, scale_percent=30):
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        return resized

    def equalize_gray_frame(self, grayframe):
        frame = cv.equalizeHist(grayframe)
        return frame

    def equalize_frame(self, frame, channels):
        ch1, ch2, ch3 = cv.split(frame)
        if channels[0]:
            ch1 = cv.equalizeHist(ch1)
        if channels[1]:
            ch2 = cv.equalizeHist(ch2)
        if channels[2]:
            ch3 = cv.equalizeHist(ch3)
        frame = cv.merge((ch1, ch2, ch3))
        return frame

    def clahe_gray_frame(self, frame, clipLimit=2.0, tileGridSize=(8, 8)):
        clahe = cv.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
        frame = clahe.apply(frame)
        return frame

    def clahe_frame(self, frame, channels, clipLimit=2.0, tileGridSize=(8, 8)):
        clahe = cv.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
        ch1, ch2, ch3 = cv.split(frame)
        if channels[0]:
            ch1 = clahe.apply(ch1)
        if channels[1]:
            ch2 = clahe.apply(ch2)
        if channels[2]:
            ch3 = clahe.apply(ch3)
        frame = cv.merge((ch1, ch2, ch3))
        return frame









# Get video source width and height
        # self.camera.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        # self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
        # self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        # self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
