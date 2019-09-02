from Tkinter import *

import sys, optparse, subprocess, urllib2, os, os.path, errno, zipfile, string, json, platform, shutil, tarfile, urlparse, tempfile, multiprocessing
from subprocess import Popen, PIPE
import argparse
import sys

def callWithoutPrint(cmdline):
    ret = subprocess.call(cmdline, shell=True)
    if ret != 0:
        print >> sys.stderr, 'Running: ' + cmdline + ' failed with exit code ' + str(ret) + '!'
    return ret

def call(cmdline):
    print 'Running: ' + cmdline
    callWithoutPrint(cmdline)

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

def clicked1():
   call("~/agrigpspi/agrigpspi.py run")
btn = Button(window, text="Agri gps", command=clicked1)
btn.grid(column=0, row=0)

def clicked2():
   call("~/bineuse/bineuse.py run")
btn = Button(window, text="Bineuse", command=clicked2)
btn.grid(column=1, row=0)

window.mainloop()
