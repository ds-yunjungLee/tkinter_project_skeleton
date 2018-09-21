from tkinter import *
from random import *

class Conveyor(Frame):
    def __init__(self, master, images, width):
        super(Conveyor, self).__init__()
        self.imagelist = []

        self.master = master
        self.width = width
        self.num = width*(width-1)+1
        self.images = images
        self.labels = []
        self.shuffle()
        

        # TODO
        # Label widget 생성
        for i in range(0, self.num):
            l = Label(self, ..., borderwidth=1, relief=SOLID)
            l.grid(column=i, row=1)
            self.labels.append(l)

        self.init_canvas()

    # TODO
    # marker와 FINAL 글씨를 그리는 부분. tkinter canvas 사용
    def init_canvas(self):
        
    # TODO
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.width*self.width), self.num)

    # TODO
    # 현재 이미지와 일치하는 이미지를 선택했을 경우
    def correct_match_config(self):
        # FINAL 일 떄
        if self.cur_idx == self.num - 1:
        # FINAL 바로 전 일 떄
        elif self.cur_idx == self.num - 2:
        # 그 외 일반적인 상황
        else:            

        
    # TODO
    # 현재 이미지와 일치하는 이미지를 선택하지 못했을 경우
    def wrong_match_config(self):
        # 마지막일 때
        if(self.cur_idx == 0):
            
        # FINAL일 때
        elif self.cur_idx == self.num-1:
            
        # 그 외 일반적인 상황
        else:
        

    # TODO
    # 오답 시 새로운 이미지를 추가하는 함수
    def get_new_image(self):        

    # TODO
    # 오답시 왼쪽으로 1칸씩 이동하고 새 이미지를 추가하는 함수
    def lshift_images(self, new_image):        