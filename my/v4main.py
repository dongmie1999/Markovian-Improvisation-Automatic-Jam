import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QCoreApplication
from my import v4
# import _thread
# import threading
import all1


play = False

class MainCode(all1.Impromptu, QMainWindow, v4.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        v4.Ui_MainWindow.__init__(self)
        # super().setupUi(self)
        self.setupUi(self)
        self.w_play.clicked.connect(self.go)
        self.w_key.activated[str].connect(self.set_key)
        self.w_mode.activated[str].connect(self.set_mode)
        self.w_bass.activated[str].connect(self.set_bass)
        self.w_accompany.activated[str].connect(self.set_accompany)
        self.w_time_signalture.activated[str].connect(self.set_time_signalture)
        self.actionexit.triggered.connect(QCoreApplication.instance().quit)
        self.actiondocument_2.triggered.connect(self.document)
        self.actionsetting.triggered.connect(self.setting)
        self.actionabout.triggered.connect(self.about)

    def document(self):
        text = "this is ducoment"
        QMessageBox.information(self, "Message", text, QMessageBox.Ok)

    def setting(self):
        text = "this is setting"
        QMessageBox.information(self, "Message", text, QMessageBox.Ok)

    def about(self):
        text = "author: @dongmie1999\n2020.4"
        QMessageBox.information(self, "Message", text, QMessageBox.Ok)

    def set_key(self, text):
        self.key = text

    def set_mode(self, text):
        self.mode = text

    def set_bass(self, text):
        if text == 'None':
            self.sw_bass = False
        else:
            self.sw_bass = True
            self.bass_type = int(text)

    def set_accompany(self, text):
        self.accompany_type = int(text)

    def set_time_signalture(self, text):
        self.time_signalture = text

    def go(self):
        try:
            self.bpm = int(self.w_bpm.text())
        except ValueError:
            text = "bpm should be an positive integer.\nrecommend: 70~150"
            QMessageBox.information(self, "Message", text, QMessageBox.Ok)
            return
        try:
            if not 0 < int(self.w_repeat.text()) <20:
                raise ValueError
        except ValueError:
            text = "repeat should be an positive integer.\nrecommend: 1~5"
            QMessageBox.information(self, "Message", text, QMessageBox.Ok)
            return
        self.intensity = int(self.w_intensity.value()/100)
        try:  # 是用级数表示的和弦
            for t in self.w_chord_progression.text():
                if 0 < int(t) < 8:
                    pass
                else:
                    text = "Input should be a series fo numbers.\nEach number must be between 1~7.\n" + \
                           "Example: 4321 or 4536251 or 1645"
                    QMessageBox.information(self, "Message", text, QMessageBox.Ok)
                    return
            self.chord_progression = self.w_chord_progression.text()
        except ValueError:  # 是和弦名称
            self.chord_progression = self.w_chord_progression.text().split(',')
        # print(self.checkBox.checkState())
        if self.checkBox.checkState():
            self.silent = True
        else:
            self.silent = False
        print("Song making...")
        self.write_song()
        self.mid.save_midi()
        print("Done. Start to play.")
        # for n in range(self.repeat):
        #     # 获取条目文本
        #     str_n = 'File index{0}'.format(n)
        #     # 添加文本到列表控件中
        #     self.listFile.addItem(str_n)
        #     # 实时刷新界面
        #     QApplication.processEvents()
        #     # 睡眠一秒
        #     time.sleep(1)
        # _thread.start_new_thread(self.mid.play_it())
        self.mid.play_it()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    # t1 = threading.Thread(target=md.show())
    # t2 = threading.Thread(target=md.go())
    # t1.start()
    # t1.join()
    # if play:
    #     print("play")
    #     t2.start()
    #     t2.join()
    #     play = False
    sys.exit(app.exec_())
