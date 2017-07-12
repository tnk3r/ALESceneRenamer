#!/usr/bin/python
import os
import sys

class aleParser():
    def __init__(self):
        self.parseArgs()
        if len(self.clipList) == 0:
            print "No Clips found in Directory"
            sys.exit(0)
        self.parseALE(self.arg1)

    def parseALE(self, ale):
        try:
            self.aleFile = open(ale).read()
            if self.aleFile[0:7] == "Heading":
                for line in self.aleFile.split("\r"):
                    raw = line.strip("\n").split("\t")
                    if raw[0] == "Name":
                        self.ALEscenePosition = raw.index("Scene")
                        self.ALETakePosition = raw.index("Take")
                    for clip in self.clipList:
                        if raw[0].split(".")[0] == clip.split(".")[0]:
                            cam = str(raw[0][0])
                            scene = str(raw[self.ALEscenePosition]).replace("_", "").replace("-", "")
                            take = str(raw[self.ALETakePosition])
                            original = str(self.sourceDirectory)+"/"+str(clip)
                            new = str(scene)+"_"+str(take)+"_"+str(cam)+"CAM."+clip.split(".")[1]
                            print "Renaming "+str(clip)+" to "+str(new)
                            os.system("mv "+str(original)+" "+str(self.sourceDirectory)+"/"+str(new))
            print "Completed Renaming Files!"
        except StandardError as msg:
            print str(msg)

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