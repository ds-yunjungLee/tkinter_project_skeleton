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
        self.upperframe = Frame(self.master) # maker와 final 영역
        self.upperframe.pack()
        self.conveyorframe = Frame(self.master) #label widget 영역
        self.conveyorframe.pack(side=BOTTOM)
        self.canvas_unit_width = self.images[0].width() #marker가 이동하기 위한 크기 = 타일 이미지 1개의 크기
        self.canvas_height = self.images[0].height() * 0.6 #canvas의 높이
        self.margin = 7 # marker와 final 글자위치에 사용하는 margin
        self.cur_idx = 9 # marker가 가르키는 위치

        self.shuffle()

        #TODO -> done
        # Label widget 생성
        for i, d in enumerate(self.imagelist):
            label = Label(self.conveyorframe, image=self.images[d], borderwidth=1, relief=SOLID)
            label.grid(column=i, row=1)
            self.labels.append(label)

        self.init_canvas()

    # TODO -> done
    # marker와 FINAL 글씨를 그리는 부분. tkinter canvas 사용
    def init_canvas(self):
        width = self.num * (self.canvas_unit_width + 2) - 2
        self.canvas = Canvas(self.upperframe, height=self.canvas_height, width=width, background='white')
        self.canvas.pack()
        # self.canvas.create_polygon(self.get_triangle_position(), fill='yellow', outline='black', tag='marker')
        self.draw_triangle()
        self.draw_final()

    # TODO -> done
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.width*self.width), self.num)

    # TODO
    # 현재 이미지와 일치하는 이미지를 선택했을 경우
    # return -1: fail, 0: normalcase, 1:win
    def correct_match_config(self):
        # FINAL 일 떄
        if self.cur_idx == self.num - 1:
            return 1

        # FINAL 바로 전 일 떄
        elif self.cur_idx == self.num - 2:
            self.cur_idx += 1
            self.canvas.delete("final")
            self.draw_triangle()
            return 0

        # 그 외 일반적인 상황
        else:
            self.cur_idx += 1
            self.draw_triangle()
            return 0

        
    # TODO
    # 현재 이미지와 일치하는 이미지를 선택하지 못했을 경우
    # return -1: fail, 0: normalcase, 1:win
    def wrong_match_config(self):
        # 마지막일 때
        if self.cur_idx == 0:
            return -1

        # FINAL일 때
        elif self.cur_idx == self.num-1:
            self.cur_idx -= 1
            self.lshift_images(self.get_new_image())
            self.draw_triangle()
            self.draw_final()
            return 0
            
        # 그 외 일반적인 상황
        else:
            self.cur_idx -= 1
            self.lshift_images(self.get_new_image())
            self.draw_triangle()
            return 0

    # TODO -> done
    # 오답 시 새로운 이미지를 추가하는 함수 #정확히는 return하는 함수.
    def get_new_image(self):
        new_image = sample(range(0, self.width * self.width), 1)[0]
        while new_image in self.imagelist:
            new_image = sample(range(0, self.width * self.width), 1)[0]
        return new_image

    # TODO -> need to verify
    # 오답시 왼쪽으로 1칸씩 이동하고 새 이미지를 추가하는 함수
    def lshift_images(self, new_image):
        del self.imagelist[0]
        self.imagelist.append(new_image)
        print(self.imagelist)
        for i, d in enumerate(self.imagelist):
            label = Label(self.conveyorframe, image=self.images[d], borderwidth=1, relief=SOLID)
            label.grid(column=i, row=1)
            self.labels.append(label)

    # marker 그릴 떄 position return하는 함수.
    def get_triangle_position(self):
        x = (self.cur_idx - 1) * (self.images[0].width() + 2) + self.margin
        y = self.margin
        tri_length = self.canvas_unit_width - self.margin * 2
        tri_height = self.canvas_height - self.margin * 1.5
        return (x, y, x+tri_length, y, x + (tri_length)/2, y + tri_height)

    # final 위치 알리는 함수. (1회성이라 생략가능)
    def get_final_position(self):
        x = self.num * (self.canvas_unit_width + 2)
        y = self.canvas_height / 2
        return (x, y)

    def draw_triangle(self):
        self.canvas.delete("marker")
        self.canvas.create_polygon(self.get_triangle_position(), fill='yellow', outline='black', tag='marker')

    def draw_final(self):
        self.canvas.create_text(self.get_final_position(), text='FINAL', fill='red', anchor=E, font=("calibri", 14), tag='final')

