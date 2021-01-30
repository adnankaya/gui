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















# Get video source width and height
            # self.camera.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
            # self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
            # self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
            # self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)













