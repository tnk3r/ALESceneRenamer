#!/usr/bin/python
import os
import sys


class aleParser():

    def __init__(self):
        self.parseArgs()
        if len(self.clipList) == 0:
            print "Error: No Clips found in Directory"
            sys.exit(0)
        self.parseALE(self.arg1)

    def parseALE(self, ale):
        try:
            self.aleFile = open(ale).read()
            if self.aleFile[0:7] == "Heading":
                for line in self.aleFile.split("\r"):
                    raw = line.strip("\n").split("\t")
                    if raw[0] == "Name":
                        self.scenePosition = raw.index("Scene")
                        self.takePosition = raw.index("Take")
                    for clip in self.clipList:
                        if raw[0].split(".")[0] == clip.split(".")[0]:
                            cam = str(raw[0][0])
                            try:
                                scene = str(raw[self.scenePosition]).replace("_", "").replace("-", "")
                                take = str(raw[self.takePosition])
                                original = str(self.sourceDirectory)+"/"+str(clip)
                                new = str(scene)+"_"+str(take)+"_"+str(cam)+"CAM."+clip.split(".")[1]
                                os.system("mv "+str(original)+" "+str(self.sourceDirectory)+"/"+str(new))
                                print "Renamed: "+str(clip)+" to "+str(new)
                            except StandardError as msg:
                                print "Couldn't Rename "+str(clip)+", Maybe no Scene+Take info was found: "+str(msg)
            print "Completed Renaming Files!"
        except StandardError as msg:
            print "Error Parsing ALE File: "+str(msg)

    def parseArgs(self):
        try:
            self.arg1 = sys.argv[1]
            self.sourceDirectory = sys.argv[2]
            self.clipList = os.listdir(self.sourceDirectory)
        except StandardError as msg:
            print """EXAMPLE: ALESceneRenamer.py Timeline1.ale Clips
                ALESceneRenamer.py ALE-FILE CLIPFOLDER
                """+str(msg)

parser = aleParser()