import sys
import os

s  = 'ssh stitch@10.211.55.3 -t '
pwd = os.getcwd().replace('/Users/taeukkim', 'machome')
s += '\"cd ' + pwd + '; zsh -l\"'

os.system(s)
