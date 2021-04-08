from PyQt5.Qt import *
import sys

from test import *

class Yest(QWidget,Ui_Form):
    def __init__(self):
        super(Yest,self).__init__()
        self.setupUi(self)
        self.setupU()#更新UI

    def setupU(self):#UI调整内容
        self.setWindowTitle('good')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w=Yest()
    w.show()


    sys.exit(app.exec_())  # app.exec_()为执行整个应用程序，为了告诉我们程序的退出，我们需要用sys.exit()
