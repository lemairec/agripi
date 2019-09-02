#!/usr/bin/env python

import sys, optparse, subprocess, urllib2, os, os.path, errno, zipfile, string, json, platform, shutil, tarfile, urlparse, tempfile, multiprocessing
from subprocess import Popen, PIPE
import argparse
import sys

from Tkinter import *
PATH = os.getcwd();

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


def install1():
    print(PATH + "/agrigpspi")
    if os.path.exists(PATH + "/agrigpspi"):
        call("cd ~/agrigpspi; git reset --hard; git pull")
    else:
        call("git clone https://github.com/lemairec/agrigpspi.git ~/agrigpspi; ~/agrigpspi/agrigpspi.py install")

btn = Button(window, text="install", command=install1)
btn.grid(column=0, row=1)


def update_setup():
   call("cd ~/agripi; git pull;")
   exit();
btn = Button(window, text="update setup", command=update_setup)
btn.grid(column=0, row=3)


window.mainloop()
