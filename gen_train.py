import os
import sys
import subprocess

if len(sys.argv) < 3:
    print "Usage: python gen_train.py input_folder output_folder"
    exit(1)

fi = sys.argv[1]
fo = sys.argv[2]

cmd0 = "convert -gravity center -resize 48x48  -extent 48x48 "

classes = os.listdir(fi)

os.chdir(fo)
for cls in classes:
    try:
        os.mkdir(cls)
    except:
        pass
    imgs = os.listdir(fi + cls)
    for img in imgs:
        outfile = fo + cls + "/0_" +  img
        md = ""
        md += cmd0
        md += fi + cls + "/" + img
        md += " " + outfile
        os.system(md)

        # Comment the following two lines to not have the flip
        md =  "convert "+ outfile  + " -flip " + fo + cls + "/0" +  "_flip_" + img
        os.system(md)

        #Add more values in the paranthesis to have more theta values
        for theta in (45,90,135,180,225,270):
             rotfile = fo + cls + "/"+ str(theta)
             md =  "convert -distort SRT " + str(-theta) + " " + outfile  + " " +  rotfile + "_" + img
             os.system(md)

             # Comment the following two lines to not have the flip
             md =  "convert "+ rotfile + "_" + img + " -flip " + rotfile + "_flip_" + img
             os.system(md)

