import time
import random
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import threading as thr
#3-12
#0
def ya1():
    print("model 1")
    handrand = int(random.random() * 3)
    print(handrand)
def ya2():
    print("model 2")
    handrand = int(random.random() * 3)
    print(handrand)
    count = 0
    sum = 0
    TIME = lambda: int(time.time() * 1000)
    random.seed(TIME() % 1000)
    while (count <= 10):
        timetemp1 = TIME()
        # time.sleep(1)
        timetemp2 = TIME()
        timetemp = timetemp2 - timetemp1
        sum = sum + timetemp
        print(sum)
        tttt = int(timetemp / 1000)
        sttt = str(tttt) + 's' + " " + str(float(timetemp - tttt * 1000)) + 'ms'
        count = count + 1
    tttt = int(sum / 1000)
    sttt = str(tttt) + 's' + " " + str(float(sum - tttt * 1000)) + 'ms'
    print(sttt)
    sum = 0
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load(r".\GUI\pi.ui")
        self.ui.pushButton.clicked.connect(self.start)
    def start(self):
        st = self.ui.lineEdit.text()  # 写
        st = int(st)
        if (st==1):
            self.ui.textEdit_13.setPlaceholderText("游戏开始")
            ya1()
        elif(st==2):
            self.ui.textEdit_13.setPlaceholderText("游戏开始")
            ya2()
        else:
            self.ui.textEdit_13.setPlaceholderText("没有该玩法")
def yaui():
    global stats
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()
def yasocket():
    while 1:
        data = s.recv(1024)
        data = data.decode()  # 第一参数默认utf8，第二参数默认strict
        print(data)
        if (data == jd or data == st or data == bu or data == ok):
            jdstbu(data)
if __name__ == "__main__":
    threadLock = thr.Lock()
    threads = []
    thread1 = thr.Thread(target=yaui)
    thread2 = thr.Thread(target=yasocket)
    thread1.start()
    thread2.start()
    threads.append(thread1)
    threads.append(thread2)
    for t in threads:
        t.join()
    print("Exiting")

