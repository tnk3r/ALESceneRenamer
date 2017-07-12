# ALESceneRenamer
This script will rename clips according to an ALE file.

place ALESceneRenamer.py in your $PATH

*** Example USAGE ***

$ ALESceneRenamer.py Timeline1.ale /home/tinker/Clips

Currently the files are renamed to $Scene_$Take_$CameraID.mov

Colorfront has this feature built in to it's transcoding engine, and any desired metadata is pulled from the SQL Database.

to make executable: chmod +x ALESceneRenamer.py