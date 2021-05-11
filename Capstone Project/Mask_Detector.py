from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from plyer import vibrator
from glob import glob

#from kivy.uix.boxlayout import Camera
import time


#Background color
Window.clearcolor = (1,1,1,1)
#Adjusting window sizee
Window.size = (360,640)

class MainApp(App):
    def build(self):
        #layout
        layout = BoxLayout(orientation='vertical',spacing=10,padding=40)
        
        #image
        img = Image(source='cute4.jpg')
        
        #buttons
        btn = Button(text='1.Start', font_size = 25, bold = True,size_hint=(None,None), width=270,height=50,pos_hint={'center_x':0.5},
                    on_release=self.start
                    )
        btn2 = Button(text='2.Camera', font_size = 25, bold = True,size_hint=(None,None), width=270,height=50,pos_hint={'center_x':0.5},
                    on_release=self.capture
                    )
          
        layout.add_widget(img)
        layout.add_widget(btn)
        layout.add_widget(btn2)

        return layout
    #When user pick the first option 1.Start
    def start(self,obj):
        print("Start")
        import numpy as numpy
        import cv2
        import random
        
        
        #importing the libraries and loading the essential XML files
        #path, 'C:\Users\chanh\OneDrive\Desktop\PythonWorkspace\opencv\Mask detection'
        face_cascade = cv2.CascadeClassifier('C:/Users/Daniel/Desktop/opencv/Application/haarcascade_frontalface_default.xml')
        mouth_cascade = cv2.CascadeClassifier('C:/Users/Daniel/Desktop/opencv/Application/Mouth.xml')
        bw_threshold = 80
        #set a threshold value to convert the impage pixels based on threshold value
        #bw_threshold = 80
        #setting the font style & origin co-ordinate point to write text on the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (30,30)
        weared_mask_font_color = (0,255,0)
        not_weared_mask_font_color = (0,0,255)
        thickness = 2
        font_scale = 1

        weared_mask = "PASS"
        not_weared_mask = "FAIL"

        for name in glob('C:/Users/Daniel/Desktop/opencv/Application/saveimages*'):

            img = cv2.imread(name,cv2.IMREAD_COLOR)
            #cv2.imshow('lady photo', img)
            #gray scale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor =1.1, minNeighbors = 4)
            faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 3)

            if(len(faces) == 0 and len(faces_bw) == 0):
                cv2.putText(img, "", org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
                print("")
            else:
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 10)
                    
            #Mask detection
            if(len(mouth_rects) == 0):
                cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
                
            else:
                
                for (mx,my,mw,mh) in mouth_rects:
                    if(y < my < y + h):
                        cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)
                        cv2.rectangle(img, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)
                        #break
            #vibrates the phone
            #vibrator.vibrate(time=3)
            cv2.imshow('family',img)
            cv2.waitKey(0)


        #When user pick the second option 2.Gallery
    def capture(self,obj):
        print("Camera")
        '''
        Builder.load_string(
        <CameraClick>:
            orientation: 'vertical'
            Camera:
                id: camera
                resolution: (640, 480)
                play: False
            ToggleButton:
                text: 'Play'
                on_press: camera.play = not camera.play
                size_hint_y: None
                height: '48dp'
            Button:
                text: 'Capture'
                size_hint_y: None
                height: '48dp'
                on_press: root.capture()
        )

        camera = self.ids['camera']
        camera.export_to_png("/sdcard/IMG_{}.png".format())
        print("Captured")
        return CameraClick()
        '''
MainApp().run()