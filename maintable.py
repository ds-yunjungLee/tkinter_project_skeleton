from imagebtn import *
from tkinter import *
from random import *
import time

class Maintable(Frame):
    def __init__(self, master, images, alphabet, width):
        super(Maintable, self).__init__()
        self.master = master
        self.width = width
        self.num = width * width
        self.images = images
        self.selected_image = None

        self.shuffle()

        # TODO Hun
        # 16개의 ImageButton 객체 생성 및 이벤트 핸들러 바인딩
        for i in range(0, self.width):
            for j in range(0, self.width):
                b = ImageButton(self, ..., relief=SOLID, overrelief=RIDGE, borderwidth=1)                
                b.grid(column=j, row=i)

    # TODO Yun
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.num), self.num)

    # TODO Yun
    # 마우스 눌렀을 때 이벤트 처리. 
    # 알파벳 이미지를 도형 이미지로 교체
    # event.widget.config 사용
    def show_hidden_image(self, event):
        pass

    # TODO Sun
    # 마우스 release 이벤트 처리
    # 도형 이미지를 원래 알파벳 이미지로 교체
    def hide_image(self, event):
        pass