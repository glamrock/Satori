import os
from PySide import QtCore, QtGui, QtNetwork


class ClickingLabel(QtGui.QLabel):
    clicked = QtCore.Signal()
    clicked_with_widget = QtCore.Signal(QtGui.QLabel)

    def __init__(self, *args, **kwargs):
        super(ClickingLabel, self).__init__(*args, **kwargs)
    #    self.setMouseTracking(True)

    #def mouseMoveEvent(self, event):
    #    print event.pos().x(), event.pos().y()

    def mousePressEvent(self, *args, **kwargs):
        self.clicked.emit()
        self.clicked_with_widget.emit(self)


def bridges_factory(bridge):
    edit = QtGui.QLineEdit(bridge)
    edit.setFont(font)
    edit.setStyleSheet("color:white;background:rgba(142, 116, 173, 100);border: 0px;border-radius: 5px;")
    edit.setReadOnly(True)
    return edit


class SoftwareLabel(ClickingLabel):
    def __init__(self, software_data, parent):
        super(SoftwareLabel, self).__init__()
        self._data = software_data
        self.parent = parent
        self.setText(software_data['title'])
        font = self.parent.get_default_font(14)
        #font.setUnderline(True)
        self.setFont(font)
        self.setStyleSheet("QLabel {color:white; background-color:transparent; }QLabel::hover {color:rgb(220, 220, 220);}")
        #  parent.set_shadow_effect(self)
        self._showing = False
        self.description_panel = QtGui.QWidget(self.parent)
        self.description_panel.setStyleSheet("background:rgba(142, 116, 173, 100)")
        self.description_panel.setVisible(False)
        self.description_layout = QtGui.QVBoxLayout(self.description_panel)
        self.description_layout.setContentsMargins(10,0,0,10)

        self.sha256sum_layout = QtGui.QHBoxLayout()
        self.description_layout.addLayout(self.sha256sum_layout)
        self.sha256sum_edit = QtGui.QLineEdit(self.sha256sum())
        self.sha256sum_edit.setFont(self.parent.get_default_font(8))
        self.sha256sum_edit.setStyleSheet("color:white;background:rgba(142, 116, 173, 0);border: 0px;")
        self.sha256sum_edit.setAutoFillBackground(True)
        self.sha256sum_edit.setReadOnly(True)
        label = QtGui.QLabel('sha256:')
        label.setFont(self.parent.get_default_font(8))
        label.setStyleSheet("color:white;background:rgba(142, 116, 173, 0);")
        label.setAutoFillBackground(False)
        self.sha256sum_layout.addWidget(label)
        self.sha256sum_layout.addWidget(self.sha256sum_edit)
        self.sha256sum_layout.addStretch()
        self.download_layout = QtGui.QHBoxLayout()
        self.description_layout.addLayout(self.download_layout)
        self.download_button = QtGui.QPushButton(self.description_panel)
        self.download_button.setText("Download")
        self.download_button.setIcon(QtGui.QIcon(":/icons/download.png"))
        self.download_button.setFlat(True)
        self.download_button.setStyleSheet("color:white;")
        self.download_button.setFont(self.parent.get_default_font(10))
        self.download_button.setIconSize(QtCore.QSize(30,30))
        self.download_layout.addWidget(self.download_button)
        self.download_progress = QtGui.QProgressBar()
        self.download_progress.setVisible(False)
        self.download_progress.setStyleSheet("QProgressBar {\n	background-color: transparent;\n color:white;   border-radius: 1px;\n	text-align: center;\n}\n\nQProgressBar::chunk {\n    background-color:rgb(62, 63, 94);\n	border-radius: 1px;\n	width: 1px;\n}")
        #self.download_progress.setTextVisible(False)
        self.download_progress.setFormat("Downloading %p%")
        self.download_layout.addWidget(self.download_progress)
        self.download_layout.addStretch()
        self.clicked.connect(lambda: self.set_showing(not self.showing()))
        self.download_button.clicked.connect(self.download_button_clicked)
        self.current_download = None
        self.manager = QtNetwork.QNetworkAccessManager(self.parent)

    def download_button_clicked(self):

        directory = QtGui.QFileDialog().getExistingDirectory()
        if not directory or len(directory) == 0 or not os.path.exists(directory):
            return
        self.download_button.setVisible(False)
        self.download_progress.setVisible(True)
        filename = os.path.basename(self.link())
        self.full_filename = os.path.join(directory, filename)

        url = QtCore.QUrl(self.link())
        request = QtNetwork.QNetworkRequest(url)
        self.current_download = self.manager.get(request)
        self.current_download.setReadBufferSize(1048576)
        self.connect(self.current_download, QtCore.SIGNAL("downloadProgress(qint64, qint64)"),
                     self.download_hook)
        self.current_download.downloadProgress.connect(self.download_hook)
        self.current_download.finished.connect(self.download_finished)
        self.current_download.readyRead.connect(self.download_ready_read)
        self.current_f = open(self.full_filename, 'wb')
        self.parent.exiting.connect(self.closing)

    def download_finished(self):
        self.download_progress.setVisible(False)
        self.download_button.setVisible(True)
        self.download_progress.setValue(100)
        self.current_f.close()

    def download_ready_read(self):
        self.current_f.write(self.current_download.readAll())

    def download_hook(self, bytesRead, totalBytes):
        p = (float(bytesRead) / float(totalBytes))*100
        self.download_progress.setValue(round(p))

    def set_showing(self, value):
        self._showing = value
        self.description_panel.setVisible(value)

    def showing(self):
        return self._showing

    def title(self):
        return self._data['title']

    def data(self):
        return self._data

    def is_windows(self):
        return self._data['section'] == 'windows'

    def is_linux(self):
        return self._data['section'] == 'linux'

    def is_mac(self):
        return self._data['section'] == 'mac'

    def link(self):
        return self._data['link']

    def sha256sum(self):
        return self._data['sha256']

    def closing(self):
        if self.current_download and self.current_download.isRunning():
            self.current_download.abort()
            self.current_f.close()
            os.remove(self.full_filename)

QtGui.QLabel = ClickingLabel