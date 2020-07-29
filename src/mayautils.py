import logging
import maya.cmds

import pymel.core as pmc
from pymel.core.system import Path


class RoadMakerUtils(object):
    def __init__(self,startxyz = [0,0,0]):
        self.startxyz = startxyz
        self.currentxyz = self.startxyz
        self.segmentnum = 0
        self.previouslocations = {}

    def update_starting_xyz(self, coordinates):
        """called if user clicks set location button. 
        updates the starting location and current location
        and resets the previous locations"""
        self.startxyz = coordinates
        self.currentxyz = self.startxyz
        self.segmentnum = 0
        self.previouslocations.clear()

    def update_xyz(self, coordinates):
        """called when the user clicks one of the directional arrows.
        updates the current location and previous location"""
        self.previouslocations[self.segmentnum] = self.currentxyz
        self.segmentnum += 1
        self.currentxyz = coordinates
    
    def undo_segment(self):
        """deltes the item at the curent location
        assigns the preveious loaction to the current location
        deletes the previous location"""
        previoussegnum = self.segmentnum - 1
        self.currentxyz = self.previouslocations[previoussegnum]
        del self.previouslocations[previoussegnum]

    def up_segment(self):
        """create a road segment rotated 90 degrees and -1 in Z direction
        if currentxyz is equal to starting xyz
            create road segment rotated 90 degrees at starting location
        call update xyz"""
        if self.currentxyz == self.startxyz:
            maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
            startcube = self.find_cube(self.segmentnum)
            maya.cmds.move(self.startxyz[0], self.startxyz[1], self.currentxyz[2], 
                           startcube)
        self.update_xyz([self.currentxyz[0], self.currentxyz[1], self.currentxyz[2] - 1])
        maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
        cube = self.find_cube(self.segmentnum)
        maya.cmds.move(self.currentxyz[0], self.currentxyz[1], self.currentxyz[2], cube)

    def down_segment(self):
        """create a road segment rotated 90 degrees and +1 in Z direction
        if currentxyz is equal to starting xyz
            create road segment rotated 90 degrees at starting location
        call update xyz"""
        if self.currentxyz == self.startxyz:
            maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
            startcube = self.find_cube(self.segmentnum)
            maya.cmds.move(self.startxyz[0], self.startxyz[1], self.currentxyz[2], 
                           startcube)
        self.update_xyz([self.currentxyz[0], self.currentxyz[1], self.currentxyz[2] + 1])
        maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
        cube = self.find_cube(self.segmentnum)
        maya.cmds.move(self.currentxyz[0], self.currentxyz[1], self.currentxyz[2], cube)
    
    def right_segment(self):
        """create a road segment +1 in X direction
        if currentxyz is equal to starting xyz
            create road segment at starting location
        call update xyz"""
        if self.currentxyz == self.startxyz:
            maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
            startcube = self.find_cube(self.segmentnum)
            maya.cmds.move(self.startxyz[0], self.startxyz[1], self.currentxyz[2], 
                           startcube)
        self.update_xyz([self.currentxyz[0] + 1, self.currentxyz[1], self.currentxyz[2]])
        maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
        cube = self.find_cube(self.segmentnum)
        maya.cmds.move(self.currentxyz[0], self.currentxyz[1], self.currentxyz[2], cube)

    def left_segment(self):
        """create a road segment -1 in X direction
        if currentxyz is equal to starting xyz
            create road segment at starting location
        call update xyz"""
        if self.currentxyz == self.startxyz:
            maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
            startcube = self.find_cube(self.segmentnum)
            maya.cmds.move(self.startxyz[0], self.startxyz[1], self.currentxyz[2], 
                           startcube)
        self.update_xyz([self.currentxyz[0] - 1, self.currentxyz[1], self.currentxyz[2]])
        maya.cmds.polyCube(name = "RoadSegment" + str(self.segmentnum))
        cube = self.find_cube(self.segmentnum)
        maya.cmds.move(self.currentxyz[0], self.currentxyz[1], self.currentxyz[2], cube)

    def find_cube(self, segmentnum):
        return maya.cmds.ls('RoadSegment' + str(segmentnum))
