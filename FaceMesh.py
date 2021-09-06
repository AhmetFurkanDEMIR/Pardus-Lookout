import cv2
import mediapipe as mp
from gi.repository import Notify
import os
import datetime

Path = "{}/parduspng.ico".format(os.getcwd())

class FaceMesh():

    def __init__(self):

        self.camera = cv2.VideoCapture(0)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_face_mesh = mp.solutions.face_mesh
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        self.FaceMesh = self.mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=99, min_detection_confidence=0.6)

        self.Privacy = 0
        self.Sentry = 0
        self.Sleep = 0
        self.ToleratedFaces = 1
        self.StartTime = ""
        self.FinishTime = ""
        self.InactivityTime = 2

        Notify.init("Pardus Lookout")

        self.Action = ""
        self.notificationCo = 500
        self.notificationSl = 500
        self.notificationSe = 500
        self.startTimeMinute = 0
        self.prewTime = 0
        self.countTime = 0

    def readFrame(self):

        self.success, self.frame = self.camera.read()

        if not self.success:
            return

        self.frame = cv2.cvtColor(cv2.flip(self.frame, 1), cv2.COLOR_BGR2RGB)
        self.frame.flags.writeable = False
        self.results = self.FaceMesh.process(self.frame)

        self.frame.flags.writeable = True

        if self.results.multi_face_landmarks:

            self.startTimeMinute = 0

            if self.Sentry == 1:

                self.StartTemp = self.StartTime.split(" ")
                self.StartYeras = self.StartTemp[0]
                self.minuteStart = int(self.StartTemp[1].split(":")[1])

                if self.StartTemp[2]=="PM":
                    self.StartHours = 12+int(self.StartTemp[1].split(":")[0])

                else:
                    self.StartHours = int(self.StartTemp[1].split(":")[0])

                self.FinishTemp = self.FinishTime.split(" ")
                self.FinishYeras = self.FinishTemp[0]
                self.minuteFinish = int(self.FinishTemp[1].split(":")[1])
                
                if self.FinishTemp[2]=="PM":
                    self.FinishHours = 12+int(self.FinishTemp[1].split(":")[0])

                else:
                    self.FinishHours = int(self.FinishTemp[1].split(":")[0])
                
                self.datetime = datetime.datetime.now()
                self.year = self.datetime.year
                self.month = self.datetime.month
                self.day = self.datetime.day
                self.hour = self.datetime.hour
                self.minute = self.datetime.minute

                if int(self.StartYeras.split("/")[0])<= self.day and int(self.FinishYeras.split("/")[0])>= self.day:

                    if int(self.StartYeras.split("/")[1])<= self.month and int(self.FinishYeras.split("/")[1])>= self.month:

                        if int("20"+self.StartYeras.split("/")[2])<= self.year and int("20"+self.FinishYeras.split("/")[2])>= self.year:
   
                            if self.StartHours <= self.hour and self.FinishHours >= self.hour:

                                if (self.StartHours < self.hour or self.minuteStart <= self.minute) and (self.FinishHours > self.hour or self.minuteFinish >= self.minute):

                                    if self.Action=="Warn":

                                        if self.notificationSe==500:

                                            n = Notify.Notification.new("Security Breach", "Your computer is being watched", "{}".format(Path))
                                            n.show()
                                            self.notificationSe=0

                                        else:

                                            self.notificationSe+=1

                                    elif self.Action=="Suspend":

                                        os.system("systemctl suspend")

                                    elif self.Action=="ShutDown":

                                        os.system("systemctl poweroff")

            for count, face_landmarks in enumerate(self.results.multi_face_landmarks):

                if self.Privacy==1:

                    if count+1 > self.ToleratedFaces:

                        if self.Action=="Warn":

                            if self.notificationCo==500:

                                n = Notify.Notification.new("Security Breach", "Your computer is being watched", "{}".format(Path))
                                n.show()
                                self.notificationCo=0

                            else:

                                self.notificationCo+=1

                        elif self.Action=="Suspend":

                            os.system("systemctl suspend")

                        elif self.Action=="ShutDown":

                            os.system("systemctl poweroff")

	        
                self.mp_drawing.draw_landmarks(
	            	image=self.frame,
	            	landmark_list=face_landmarks,
	            	connections=self.mp_face_mesh.FACEMESH_TESSELATION,
	            	landmark_drawing_spec=None,
	            	connection_drawing_spec=self.mp_drawing_styles
	            	.get_default_face_mesh_tesselation_style())


        else:

            if self.Sleep==1:

                self.datetime = datetime.datetime.now()

                if self.startTimeMinute == 0:

                    self.startTimeMinute = 1
                    self.countTime = 0
                    self.prewTime = self.datetime.minute

                else:

                    if self.prewTime!=self.datetime.minute:

                        self.countTime+=1
                        self.prewTime=self.datetime.minute

                    elif self.countTime>=self.InactivityTime:

                        if self.Action=="Warn":

                            if self.notificationSl==500:

                                n = Notify.Notification.new("Power Alert", "We noticed that your computer is not being used", "{}".format(Path))
                                n.show()
                                self.notificationSl=0

                            else:

                                self.notificationSl+=1

                        elif self.Action=="Suspend":

                            os.system("systemctl suspend")

                        elif self.Action=="ShutDown":

                            os.system("systemctl poweroff")

        return self.frame
