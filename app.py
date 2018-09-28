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

        # TODO, Hun
        upperframe = Frame(master)
        upperframe.pack()
        self.table = Maintable(upperframe, self.figure_images, self.alphabet_images, self.num, self)
        self.table.pack()

        # TODO, Yun
        # Conveyor 객체 생성
        bottomframe = Frame(master)
        bottomframe.pack(side=BOTTOM)
        self.conveyor = Conveyor(bottomframe, self.resized_images, self.num)

    def load_images(self):
        self.figure_images = list(Image.open("picture\\%d.JPG" % (i+1)) for i in range(self.num*self.num))
        self.alphabet_images = list(PhotoImage(file="alphabet\\%d.GIF" % (i+1)) for i in range(self.num*self.num))
        self.resized_images = list(ImageTk.PhotoImage(self.figure_images[i].resize((50, 50), Image.ANTIALIAS)) for i in range(self.num*self.num))
        self.figure_images = list(ImageTk.PhotoImage(self.figure_images[i]) for i in range(self.num*self.num))

    # TODO Hun
    # MainTable에서 선택한 도형 이미지와 Conveyor에서 Marker가 현재 가리키는 이미지를 비교한 후 비교 결과에 따라 처리한다.
    def compare_images(self):
        conveyor_image = self.conveyor.imagelist[self.conveyor.cur_idx]
        print('conveyor_imglist: ', self.conveyor.imagelist)
        table_image = self.table.selected_image
        print('cur_idx:', self.conveyor.cur_idx)
        print('conveyor_image:', conveyor_image)
        print('table_image:', table_image)
        print('------')
        if conveyor_image == table_image:
            ret = self.conveyor.correct_match_config()
        else:
            ret = self.conveyor.wrong_match_config()

        self.finish(ret)

    # TODO Yun
    # 종료 조건 만족 시 실행
    def finish(self, win):
        if abs(win) == 1:
            exit()
