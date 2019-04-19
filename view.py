# -*- coding: utf-8 -*-
import PyQt5.sip
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
import sys
from utility.thread_manage import Thread_Manage
from ui import download
from model import Model


class Updater(QtWidgets.QWidget):
    signal_version_fresh = pyqtSignal(str, str)
    signal_update_tips = pyqtSignal(str)
    signal_update_log = pyqtSignal(str)

    signal_idle = pyqtSignal()
    signal_new = pyqtSignal()
    signal_downloading = pyqtSignal(int)
    signal_downloaded = pyqtSignal()

    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.parent = parent
        self.model = Model(self)
        # 调整页面
        self.ui = download.Ui_Form_download()
        self.ui.setupUi(self)
        #
        self.signal_slots_init()
        self.thread_manage = Thread_Manage()

        # 必要信息
        self.req_check_update()
        self.module_init()

    def module_init(self):
        self.ui.plainTextEdit_update_log.setReadOnly(True)

    def signal_slots_init(self):
        self.ui.pushButton_update.clicked.connect(self.model.req_update)

        # signal
        self.signal_version_fresh.connect(self.ui_version_fresh)
        self.signal_update_tips.connect(self.ui.label_tips.setText)
        self.signal_update_log.connect(self.ui_update_log_fresh)

        self.signal_idle.connect(self.ui_idle)
        self.signal_new.connect(self.ui_new)
        self.signal_downloading.connect(self.ui_downloading)
        self.signal_downloaded.connect(self.ui_downloaded)

    def req_check_update(self):
        self.model.req_query_update()

    def ui_idle(self):
        self.ui.pushButton_update.setText('Check')
        self.ui.progressBar_update.setValue(0)

    def ui_new(self):
        self.ui.pushButton_update.setText('Download')
        self.ui.progressBar_update.setValue(0)

    def ui_downloading(self, progress):
        self.ui.pushButton_update.setText('Downloading')
        self.ui.progressBar_update.setValue(progress)

    def ui_downloaded(self):
        self.ui.pushButton_update.setText('Update')
        self.ui.progressBar_update.setValue(100)

    def ui_version_fresh(self, cur_ver, latest_ver):
        self.ui.label_current_version.setText(cur_ver)
        self.ui.label_latest_version.setText(latest_ver)

    def ui_update_log_fresh(self, text):
        self.ui.plainTextEdit_update_log.setPlainText(text)


class PyQtUpdater(QtWidgets.QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.updater = Updater(self)

    def run(self):
        self.updater.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyQtUpdater()
    window.run()
    sys.exit(app.exec_())