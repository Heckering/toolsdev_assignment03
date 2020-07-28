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
        self.scene = mayautils.SceneFile()
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
        # Direction 
        self.direction_lbl = QtWidgets.QLabel("Direction:")
        self.left_btn = QtWidgets.QPushButton("<")
        self.up_btn = QtWidgets.QPushButton("^")
        self.down_btn = QtWidgets.QPushButton("v")
        self.right_btn = QtWidgets.QPushButton(">")
        self.undo_btn = QtWidgets.QPushButton("Undo")
        # Finish
        self.finish_btn = QtWidgets.QPushButton("Finish")
        """create widgets for our ui"""
        """self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 40px")
        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.dir_le.setText(self.scene.dir)
        self.brows_btn = QtWidgets.QPushButton("Browse...")
        self.descriptor_lbl = QtWidgets.QLabel("Descriptor")
        self.descriptor_le = QtWidgets.QLineEdit()
        self.descriptor_le.setText(self.scene.descriptor)
        self.version_lbl = QtWidgets.QLabel("Version")
        self.version_spinbox = QtWidgets.QSpinBox()
        self.version_spinbox.setValue(self.scene.version)
        self.ext_lbl = QtWidgets.QLabel("Extension")
        self.ext_le = QtWidgets.QLineEdit()
        self.ext_le.setText(self.scene.ext)
        self.save_btn = QtWidgets.QPushButton("Save")
        self.increment_save_btn = QtWidgets.QPushButton("Increment and Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")"""

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
        """lay out our widgets in the ui"""
        """self.directory_lay = QtWidgets.QHBoxLayout()
        self.directory_lay.addWidget(self.dir_lbl)
        self.directory_lay.addWidget(self.dir_le)
        self.directory_lay.addWidget(self.brows_btn)

        self.descriptor_lay = QtWidgets.QHBoxLayout()
        self.descriptor_lay.addWidget(self.descriptor_lbl)
        self.descriptor_lay.addWidget(self.descriptor_le)

        self.version_lay = QtWidgets.QHBoxLayout()
        self.version_lay.addWidget(self.version_lbl)
        self.version_lay.addWidget(self.version_spinbox)

        self.ext_lay = QtWidgets.QHBoxLayout()
        self.ext_lay.addWidget(self.ext_lbl)
        self.ext_lay.addWidget(self.ext_le)

        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.increment_save_btn)
        self.bottom_btn_lay.addWidget(self.save_btn)
        self.bottom_btn_lay.addWidget(self.cancel_btn)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.main_layout.addLayout(self.directory_lay)
        self.main_layout.addLayout(self.descriptor_lay)
        self.main_layout.addLayout(self.version_lay)
        self.main_layout.addLayout(self.ext_lay)

        self.main_layout.addStretch()

        self.main_layout.addLayout(self.bottom_btn_lay)

        self.setLayout(self.main_layout)"""

    def create_connections(self):
        """connects our witget signals to slots"""
        self.finish_btn.clicked.connect(self.cancel)
        """self.save_btn.clicked.connect(self.save)
        self.increment_save_btn.clicked.connect(self.increment_save)"""

    def _populate_sceenfile_properties(self):
        """populates the scenfile objects properties from the ui"""
        self.scene.dir = self.dir_le.text()
        self.scene.descriptor = self.descriptor_le.text()
        self.scene.version = self.version_spinbox.value()
        self.scene.ext = self.ext_le.text()

    @QtCore.Slot()
    def save(self):
        """saves the scene file"""
        self._populate_sceenfile_properties()
        self.scene.save()

    @QtCore.Slot()
    def increment_save(self):
        """Automatically finds the next available version on disk and saves up"""
        self._populate_sceenfile_properties()
        self.scene.increment_and_save()

    @QtCore.Slot()
    def cancel(self):
        """quits the dialog"""
        self.close()