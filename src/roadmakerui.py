import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

import mayautils


def maya_main_window():
    """return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class RoadMakerUI(QtWidgets.QDialog):
    """simple UI Class"""

    def __init__(self):
        """constructor"""
        # Passing the object RoadMakerUI as an argument to super()
        # makes this line python 2 and 3 compatible
        super(RoadMakerUI, self).__init__(parent=maya_main_window())
        self.roadmaker = mayautils.RoadMakerUtils()
        self.setWindowTitle("Road Maker")
        self.resize(500, 200)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_witgets()
        self.create_layout()
        self.create_connections()
    
    def create_witgets(self):
        # Title
        self.title_lbl = QtWidgets.QLabel("Road Maker")
        self.title_lbl.setStyleSheet("font: bold 40px")
        # Location Picker
        self.location_lbl = QtWidgets.QLabel("Start at Location:")
        self.x_location_lbl = QtWidgets.QLabel("X:")
        self.x_spinbox = QtWidgets.QSpinBox()
        self.y_location_lbl = QtWidgets.QLabel("Y:")
        self.y_spinbox = QtWidgets.QSpinBox()
        self.z_location_lbl = QtWidgets.QLabel("Z:")
        self.z_spinbox = QtWidgets.QSpinBox()
        self.set_btn = QtWidgets.QPushButton("Set Locaton")
        # Spinbox Ranges
        self.x_spinbox.setRange(-2147483647,2147483647)
        self.y_spinbox.setRange(-2147483647,2147483647)
        self.z_spinbox.setRange(-2147483647,2147483647)
        # Direction 
        self.direction_lbl = QtWidgets.QLabel("Direction:")
        self.left_btn = QtWidgets.QPushButton("<")
        self.up_btn = QtWidgets.QPushButton("^")
        self.down_btn = QtWidgets.QPushButton("v")
        self.right_btn = QtWidgets.QPushButton(">")
        self.undo_btn = QtWidgets.QPushButton("Undo")
        # Finish
        self.finish_btn = QtWidgets.QPushButton("Finish")

    def create_layout(self):
        # Start Location Layout
        self.srt_location_layout = QtWidgets.QHBoxLayout()
        self.srt_location_layout.addWidget(self.location_lbl)
        self.srt_location_layout.addWidget(self.x_location_lbl)
        self.srt_location_layout.addWidget(self.x_spinbox)
        self.srt_location_layout.addWidget(self.y_location_lbl)
        self.srt_location_layout.addWidget(self.y_spinbox)
        self.srt_location_layout.addWidget(self.z_location_lbl)
        self.srt_location_layout.addWidget(self.z_spinbox)
        self.srt_location_layout.addWidget(self.set_btn)
        # Direction Layout
        self.direction_layout_upper = QtWidgets.QHBoxLayout()
        self.direction_layout_upper.addWidget(self.up_btn)
        self.direction_layout_center = QtWidgets.QHBoxLayout()
        self.direction_layout_center.addWidget(self.direction_lbl)
        self.direction_layout_center.addWidget(self.left_btn)
        self.direction_layout_center.addWidget(self.right_btn)
        self.direction_layout_center.addWidget(self.undo_btn)
        self.direction_layout_lower = QtWidgets.QHBoxLayout()
        self.direction_layout_lower.addWidget(self.down_btn)
        self.direction_layout = QtWidgets.QVBoxLayout()
        self.direction_layout.addLayout(self.direction_layout_upper)
        self.direction_layout.addLayout(self.direction_layout_center)
        self.direction_layout.addLayout(self.direction_layout_lower)
        # Finish Button Layout
        self.finish_btn_layout = QtWidgets.QHBoxLayout()
        self.finish_btn_layout.addWidget(self.finish_btn)
        # Main Layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.main_layout.addLayout(self.srt_location_layout)
        self.main_layout.addLayout(self.direction_layout)
        self.main_layout.addLayout(self.finish_btn_layout)
        # Finalize Layout
        self.setLayout(self.main_layout)

    def create_connections(self):
        """connects our witget signals to slots"""
        self.finish_btn.clicked.connect(self.cancel)
        self.up_btn.clicked.connect(self.up_seg)
        self.down_btn.clicked.connect(self.down_seg)
        self.left_btn.clicked.connect(self.left_seg)
        self.right_btn.clicked.connect(self.right_seg)
        self.undo_btn.clicked.connect(self.undo_seg)
        self.set_btn.clicked.connect(self.set_start)

    @QtCore.Slot()
    def set_start(self):
        coordinates = [int(self.x_spinbox.text()),
                       int(self.y_spinbox.text()),
                       int(self.z_spinbox.text())]
        self.roadmaker.update_starting_xyz(coordinates)

    @QtCore.Slot()
    def up_seg(self):
        self.roadmaker.up_segment()
    
    @QtCore.Slot()
    def down_seg(self):
        self.roadmaker.down_segment()

    @QtCore.Slot()
    def left_seg(self):
        self.roadmaker.left_segment()

    @QtCore.Slot()
    def right_seg(self):
        self.roadmaker.right_segment()

    @QtCore.Slot()
    def undo_seg(self):
        self.roadmaker.undo_segment()

    @QtCore.Slot()
    def cancel(self):
        """quits the dialog"""
        self.roadmaker.finish_segments()
        self.close()