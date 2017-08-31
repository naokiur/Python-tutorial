import shutil
import os

shutil.copyfile("data.db", "archive.db")
os.system("ls")
os.mkdir("dst")
shutil.move("archive.db", "dst")
os.system("ls -R")
shutil.rmtree("dst")

