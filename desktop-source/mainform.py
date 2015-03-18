import json
import os

__author__ = 'sashgorokhov'

from PySide import QtGui, QtCore
import utils
from mainform_ui import Ui_MainForm
from hashlib import sha256


def sha256sum(file_path):
    sum = sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024*256)
            if not data:
                break
            sum.update(data)
    return sum.hexdigest()


class MainForm(QtGui.QWidget, Ui_MainForm):
    exiting = QtCore.Signal()

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.show_main_page()
        #self.setFixedSize(self.size())

        self.select_folder_button.clicked.connect(self.select_folder_button_clicked)
        self.select_file_button.clicked.connect(self.select_file_button_clicked)

        self.language_switch.setVisible(False)
        self.language_switch_2.setVisible(False)
        self.language_switch_3.setVisible(False)
        self.language_switch_4.setVisible(False)
        self.language_switch_5.setVisible(False)

        self.bridges_right_menu_button.clicked.connect(self.show_bridges_page)
        self.bridges_right_menu_button_2.clicked.connect(self.show_bridges_page)
        self.bridges_right_menu_button_3.clicked.connect(self.show_bridges_page)

        self.guides_right_menu_button.clicked.connect(self.show_guides_page)
        self.guides_right_menu_button_2.clicked.connect(self.show_guides_page)
        self.guides_right_menu_button_3.clicked.connect(self.show_guides_page)

        self.home_right_menu_button.clicked.connect(self.show_main_page)
        self.home_right_menu_button_2.clicked.connect(self.show_main_page)
        self.home_right_menu_button_3.clicked.connect(self.show_main_page)
        self.home_right_menu_button_4.clicked.connect(self.show_main_page)

        self.verify_right_menu_button.clicked.connect(self.show_verify_page)
        self.verify_right_menu_button_2.clicked.connect(self.show_verify_page)
        self.verify_right_menu_button_3.clicked.connect(self.show_verify_page)

        self.software_right_menu_button.clicked.connect(self.show_software_page)
        self.software_right_menu_button_2.clicked.connect(self.show_software_page)
        self.software_right_menu_button_3.clicked.connect(self.show_software_page)

        self.software_label.clicked.connect(self.show_software_page)
        #self.guides_label.clicked.connect(self.show_guides_page)
        self.bridges_label.clicked.connect(self.show_bridges_page)
        self.verify_label.clicked.connect(self.show_verify_page)

        self.set_shadow_effect(self.software_label)
        #self.set_shadow_effect(self.guides_label)
        self.set_shadow_effect(self.bridges_label)
        self.set_shadow_effect(self.verify_label)
        self.set_shadow_effect(self.get_bridges_label)
        self.set_shadow_effect(self.verify_label_2)
        self.set_shadow_effect(self.generate_label)
        self.set_shadow_effect(self.select_file_button)
        self.set_shadow_effect(self.select_folder_button)

        self.verify_scroll_area.setVisible(False)
        self.verify_layout = QtGui.QVBoxLayout(self.verify_scroll_area_widget_contents)
        self.verify_scroll_area.setWidget(self.verify_layout.widget())
        self.verify_layout.setSpacing(10)

        self.fill_software_list()
        self.fill_bridges_list()

        self.software_verify_list = list()
        with open('detector.json', 'r') as f:
            self.software_verify_list = json.load(f)
        self.software_verify_dict = {i['sha256sum']: i['title'] for i in self.software_verify_list}

        self.guides_right_menu_button.setVisible(False)
        self.guides_right_menu_button_2.setVisible(False)
        self.guides_right_menu_button_3.setVisible(False)


    def get_default_font(self, point_size=14, bold=False):
        name = "Segoe UI"
        if bold:
            name += " Black"
        else:
            name += " Semibold"
        font = QtGui.QFont(name)
        font.setPointSize(point_size)
        return font

    def fill_software_list(self):
        self.software_layout = QtGui.QVBoxLayout(self.software_scrollarea_widgetcontents)
        self.software_layout.setContentsMargins(5, 5, 5, 5)

        font = self.get_default_font(28)

        def label_factory(text):
            label = utils.ClickingLabel()
            label.setText(text)
            label.setStyleSheet("color:white;background-color:transparent;")
            label.setFont(font)
            self.set_shadow_effect(label)
            return label

        def layout_factory():
            layout = QtGui.QVBoxLayout(self.software_layout.widget())
            layout.setContentsMargins(10, 5, 5, 5)
            return layout

        self.windows_label = label_factory("Windows")
        self.software_layout.addWidget(self.windows_label)
        self.windows_layout = layout_factory()
        self.software_layout.addLayout(self.windows_layout)

        self.linux_label = label_factory("Linux")
        self.software_layout.addWidget(self.linux_label)
        self.linux_layout = layout_factory()
        self.software_layout.addLayout(self.linux_layout)

        self.mac_label = label_factory("MacOS")
        self.software_layout.addWidget(self.mac_label)
        self.mac_layout = layout_factory()
        self.software_layout.addLayout(self.mac_layout)

        self.software_layout.addStretch()

        self.software_scrollarea.setWidget(self.software_layout.widget())

        with open('software.json', 'r') as f:
            software_list = json.load(f)
        for soft in software_list:
            software_label = utils.SoftwareLabel(soft, self)
            if software_label.is_windows():
                self.windows_layout.addWidget(software_label)
                self.windows_layout.addWidget(software_label.description_panel)
            if software_label.is_linux():
                self.linux_layout.addWidget(software_label)
                self.linux_layout.addWidget(software_label.description_panel)
            if software_label.is_mac():
                self.mac_layout.addWidget(software_label)
                self.mac_layout.addWidget(software_label.description_panel)
        if self.windows_layout.count()==0:
            self.windows_label.setVisible(False)
        if self.linux_layout.count()==0:
            self.linux_label.setVisible(False)
        if self.mac_layout.count()==0:
            self.mac_label.setVisible(False)

    def fill_bridges_list(self):
        self.bridges_layout = QtGui.QVBoxLayout(self.bridges_scrollarea_widget_contents)
        self.bridges_layout.setContentsMargins(5, 5, 5, 5)
        font = self.get_default_font(8)

        def bridges_factory(bridge):
            edit = QtGui.QLineEdit(bridge)
            edit.setFont(font)
            edit.setStyleSheet("color:white;background:rgba(142, 116, 173, 100);border: 0px;border-radius: 5px;")
            edit.setReadOnly(True)
            return edit

        with open("bridges.json", 'r') as f:
            bridges_list = json.load(f)

        for bridge in bridges_list:
            bridge_widget = bridges_factory(bridge)
            self.bridges_layout.addWidget(bridge_widget)

        self.bridges_layout.addStretch()
        self.software_scrollarea.setWidget(self.software_layout.widget())

    def set_shadow_effect(self, widget, radius=5, offset=(1, 1)):
        shadow_effect = QtGui.QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(radius)
        shadow_effect.setColor(QtGui.QColor("#000000"))
        shadow_effect.setOffset(*offset)
        widget.setGraphicsEffect(shadow_effect)

    def closeEvent(self, event):
        self.exiting.emit()
        event.accept()

    def show_main_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_software_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_guides_page(self, guide_id=0):
        self.stackedWidget.setCurrentIndex(2)
        self.guides_stacked_widget.setCurrentIndex(guide_id)

    def show_bridges_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_verify_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def select_folder_button_clicked(self):
        directory = QtGui.QFileDialog().getExistingDirectory()
        if not directory or len(directory) == 0 or not os.path.exists(directory):
            return
        file_list = list(filter(lambda x: os.path.isfile(x), map(lambda x: os.path.join(directory, x), os.listdir(directory))))
        if len(file_list) > 0:
            self.check_sha_sums(file_list)

    def select_file_button_clicked(self):
        file_path = QtGui.QFileDialog().getOpenFileName()[0]
        if not file_path or len(file_path) == 0 or not os.path.exists(file_path):
            return
        self.check_sha_sums([file_path])

    def clear_verify_layout(self):
        for i in reversed(range(self.verify_layout.count())):
            widget = self.verify_layout.itemAt(i)
            if isinstance(widget, QtGui.QLayout):
                for j in reversed(range(widget.count())):
                    widget.itemAt(j).widget().deleteLater()
            if isinstance(widget, QtGui.QSpacerItem):
                self.verify_layout.removeItem(widget)
            else:
                try:
                    widget.deleteLater()
                except:
                    pass

    def check_sha_sums(self, files):
        self.verify_scroll_area.setVisible(True)
        self.clear_verify_layout()

        def label_factory(text):
            label = QtGui.QLabel(text)
            label.setStyleSheet("color:white;")
            label.setFont(self.get_default_font(10, True))
            return label

        def bridges_factory(bridge):
            edit = QtGui.QLineEdit(bridge)
            edit.setFont(self.get_default_font(10))
            edit.setStyleSheet("color:white;background:rgba(142, 116, 173, 100);border: 0px;border-radius: 5px;")
            edit.setReadOnly(True)
            return edit

        for file_path in files:
            sum = sha256sum(file_path)
            result = self.search_software(sum)
            layout = QtGui.QVBoxLayout()
            layout.setSpacing(3)
            sum_label = bridges_factory(sum)
            filename_label = label_factory(os.path.basename(file_path))
            filename_label.setStyleSheet("background-color:transparent;color:white;")
            layout.addWidget(filename_label)
            layout.addWidget(sum_label)
            if result:
                found_label = label_factory("Software found: " + result)
                found_label.setStyleSheet("font-style: italic; color: rgb(24, 181, 24);background-color:transparent;")
                found_label.setFont(self.get_default_font(14))
                layout.addWidget(found_label)
            self.verify_layout.addLayout(layout)
        if 1 <= self.verify_layout.count() <= 3:
            self.verify_scroll_area.setFixedHeight(85*self.verify_layout.count())
        else:
            self.verify_scroll_area.setFixedHeight(self.height()-200)
        if self.verify_layout.count() > 0:
            self.verify_layout.addStretch()

    def search_software(self, sha256sum):
        if sha256sum in self.software_verify_dict:
            return self.software_verify_dict[sha256sum]