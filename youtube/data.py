import matplotlib
import matplotlib.font_maneger as fm
import matplotlib.pyplot as pyplot
import pandas as pd

mydir ='/mnt/c/users/k-masa0921/sources/OneDrive - Kyushu Institute Of Technolgy/4年/池永研究室/教材/20200822_Pythonseminer'

font_file = mydir + 'IPAexfont00401/ipaexg.ttf'
fm.fontManeger.addfont(font_file)

matplotlib.rc('font',family="IPAexGothic")