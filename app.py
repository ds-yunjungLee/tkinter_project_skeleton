from maintable import *
from conveyor import *
from PIL import Image, ImageTk
from tkinter.messagebox import *

class App(Frame):
    def __init__(self, master, num):
        super(App, self).__init__()
        self.master = master
        self.num = num
        self.load_images()

        # TODO
        # Conveyor 객체 생성
        self.conveyor = 
        
        # TODO
        # MainTable 객체 생성
        self.table =         
        
    def load_images(self):
        self.figure_images = list(Image.open("picture\\%d.JPG" % (i+1)) for i in range(self.num*self.num))
        self.alphabet_images = list(PhotoImage(file="alphabet\\%d.GIF" % (i+1)) for i in range(self.num*self.num))
        self.resized_images = list(ImageTk.PhotoImage(self.figure_images[i].resize((50,50), Image.ANTIALIAS)) for i in range(self.num*self.num))
        self.figure_images = list(ImageTk.PhotoImage(self.figure_images[i]) for i in range(self.num*self.num))

    # TODO
    # MainTable에서 선택한 도형 이미지와 Conveyor에서 Marker가 현재 가리키는 이미지를 비교한 후 비교 결과에 따라 처리한다.
    def compare_images(self):        
    
    # TODO
    # 종료 조건 만족 시 실행
    def finish(self, win):       
