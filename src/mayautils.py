import logging

import pymel.core as pmc
from pymel.core.system import Path


log = logging.getLogger(__name__)
patha = Path()
"""
def main():
    print(pmc.ls(type='camera'))
    counter = 0
    while(counter<=3):
        cubexform, cubeshape = pmc.polyCube()
        cubexform.translateY.set(1.5+counter)
        counter += 1"""

class SceneFile(object):
    """Class used to to represent a DCC software scene file

    The class will be a convenient object that we can use to manipulate our 
    scene files. Examples features include the ability to predefine our naming 
    conventions and automatically increment our versions.

    Attributes:
        dir (Path, optional): Directory to the scene file. Defaults to ''.
        descriptor (str, optional): Short descriptor of the scene file. 
            Defaults to "main".
        version (int, optional): Version number. Defaults to 1.
        ext (str, optional): Extension. Defaults to "ma"

    """

    def __init__(self, dir="", descriptor="main", version=1, ext="ma"):
        #how do I find the open file
        try:
            self._dir = self.isolate_filepath()
            self.descriptor = self.isolate_descriptor()
            self.version = self.isolate_version()
            self.ext = self.isolate_ext()
        except Exception:
            self._dir = Path(dir)
            self.descriptor = descriptor
            self.version = version
            self.ext = ext

    @property
    def dir(self):
        #print("getting")
        #print(Path(self._dir))
        return Path(self._dir)

    @dir.setter
    def dir(self, arg):
        #print("setting")
        self._dir = Path(arg)

    def basename(self):
        """Return a scene file name.

        e.g. ship_001.ma, car_011.hip

        Returns:
            str: The name of the scene file.

        """
        name_pattern = "{descriptor}_{version:03d}.{ext}"
        name = name_pattern.format(descriptor=self.descriptor,
                                   version=self.version,
                                   ext=self.ext)
        return name

    def path(self):
        """The function returns a path to scene file.

        This includes the drive letter, any directory path and the file name.

        Returns:
            Path: The path to the scene file.

        """
        return Path(self.dir) / self.basename()

    def save(self):
        """Saves the scene file.

        Returns:
            Path: The path to the scene file if successful, None, otherwise.

        """
        #scenepath = "C:\\Users\\blake\\OneDrive\\Documents\\toolsdev\\toolsdev_assignment02\\assignment2_save\\"
        try:
            pmc.system.saveAs(self.path())
        except RuntimeError:
            log.warning("Missing Directories. Creating new directories")
            self.dir.makedirs_p()
            pmc.system.saveAs(self.path())


    def increment_and_save(self):
        #How do I find current newest version?
        self.version += 1
        print(self.version)
        try:
            pmc.system.saveAs(self.path())
            return self.path()
        except RuntimeError:
            log.warning("Missing Directories. Creating new directories")
            self.dir.makedirs_p()
            pmc.system.saveAs(self.path())
            return self.path()
        """Increments the version and saves the scene file.

        If existing versions of a file already exist, it should increment 
        from the largest number available in the folder.

        Returns:
            Path: The path to the scene file if successful, None, otherwise.
        """
        
    def isolate_filename(self):
        scenepath = pmc.system.sceneName() #this works, but how to I seperate the string into attributes
        filename = str(scenepath).split("/")[-1:]
        return filename
        
    def isolate_filepath(self):
        filepath = ""
        scenepath = pmc.system.sceneName() 
        splitscenepath = str(scenepath).split("/")
        splitscenepath.pop()
        for location in splitscenepath:
            filepath += location + "\\\\"
        print(filepath)
        return filepath
    
    def isolate_ext(self):
        filename = self.isolate_filename()[0]
        ext = filename.split(".")[-1:]
        print(ext[0])
        return ext[0]

    def isolate_version(self):
        filename = self.isolate_filename()[0]
        splitfilename = filename.split(".")[0]
        versionList = splitfilename.split("_")[-1:]
        version = versionList[0]
        intversion = int(version)
        print(intversion)
        return intversion

    def isolate_descriptor(self):
        filename = self.isolate_filename()[0]
        main = filename.split("_")[0]
        print(main)
        return main
