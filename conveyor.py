from tkinter import *
from random import *

class Conveyor(Frame):
    def __init__(self, master, images, width):
        super(Conveyor, self).__init__()
        self.imagelist = [] # 셔플된 이미지의 번호 저장

        self.master = master
        self.width = width
        self.num = width*(width-1)+1 #컨베이어에 넣을 이미지의 수 = 13
        self.images = images #app에서 받아온 총 16개의 resize된 이미지
        self.labels = [] #conveyerframe에 추가되는 이미지 label 위젯 리스트
        self.shuffle()

        self.upperframe = Frame(self.master) # maker와 final 영역
        self.upperframe.pack()
        self.conveyorframe = Frame(self.master) #label widget 영역
        self.conveyorframe.pack(side=BOTTOM)

        # Label widget 생성
        self.shuffle();
        for i, d in enumerate(self.imagelist):
            print(i, d)
            l = Label(self.conveyorframe, image=self.images[d], borderwidth=1, relief=SOLID)
            l.grid(column=i, row=1)
            self.labels.append(l)

        self.init_canvas()

    # TODO # Yun
    # marker와 FINAL 글씨를 그리는 부분. tkinter canvas 사용
    def init_canvas(self):
        pass

    # TODO #Sun
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.width*self.width), self.num)

    # TODO #Yun
    # 현재 이미지와 일치하는 이미지를 선택했을 경우
    def correct_match_config(self):
        # FINAL 일 떄
        if self.cur_idx == self.num - 1:
            pass
        # FINAL 바로 전 일 떄
        elif self.cur_idx == self.num - 2:
            pass
        # 그 외 일반적인 상황
        else:
            pass

        
    # TODO HUn
    # 현재 이미지와 일치하는 이미지를 선택하지 못했을 경우
    def wrong_match_config(self):
        # 마지막일 때
        if(self.cur_idx == 0):
            pass
        # FINAL일 때
        elif self.cur_idx == self.num-1:
            pass
            
        # 그 외 일반적인 상황
        else: pass
        

    # TODO Sun
    # 오답 시 새로운 이미지를 추가하는 함수
    def get_new_image(self):
        pass

    # TODO Sun
    # 오답시 왼쪽으로 1칸씩 이동하고 새 이미지를 추가하는 함수
    def lshift_images(self, new_image):
        pass