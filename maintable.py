from imagebtn import *
from tkinter import *
from random import *
import time

class Maintable(Frame):
    def __init__(self, master, images, alphabet, width, app):
        super(Maintable, self).__init__()
        self.master = master
        self.width = width
        self.num = width * width
        self.images = images
        self.alphabet = alphabet
        self.selected_image = None
        self.app = app

        self.shuffle()

        # TODO Hun
        # 16개의 ImageButton 객체 생성 및 이벤트 핸들러 바인딩
        self.buttons = []
        for i in range(0, self.width):
            for j in range(0, self.width):
                b = ImageButton(self, image=self.alphabet[i*width + j],
                                hidden_image=self.images[self.imagelist[i*self.width + j]],
                                relief=SOLID, overrelief=RIDGE, borderwidth=1)
                b.grid(column=j, row=i)
                b.bind('<Button-1>', self.make_show_hidden_image(i*self.width + j))
                b.bind('<ButtonRelease-1>', self.make_hide_image(i*self.width + j))
                self.buttons.append(b)


    # TODO Yun
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.num), self.num)

    # TODO Yun
    # 마우스 눌렀을 때 이벤트 처리. 
    # 알파벳 이미지를 도형 이미지로 교체
    # event.widget.config 사용

    def make_show_hidden_image(self, location):
        def show_hidden_image(event):
            #print('image_list in maintable:', self.imagelist)
            self.selected_image = self.imagelist[location]
            self.buttons[location].configure(image=self.images[self.selected_image])
        return show_hidden_image


    # TODO Sun
    # 마우스 release 이벤트 처리
    # 도형 이미지를 원래 알파벳 이미지로 교체
    def make_hide_image(self, location):
        def show_hide_image(event):
            self.buttons[location].configure(image=self.alphabet[location])
            self.app.compare_images()
        return show_hide_image
