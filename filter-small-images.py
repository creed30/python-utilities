from PIL import Image
import sys
import glob
import os

print "This is the directory of the pictures: ", sys.argv[1]
arr = glob.glob(sys.argv[1] + "/*."+sys.argv[2])
x = int(sys.argv[3])
y = int(sys.argv[4])

for file in arr:
    im = Image.open(file)
    if im.size[0] < x and im.size[1] < y:
        os.rename(file, os.path.dirname(os.path.abspath(file)) +
                  "/toosmall/"+os.path.basename(file))
