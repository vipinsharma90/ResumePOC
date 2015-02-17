from tagParser import readOptionValue
import os
import sys
from commands import *

#print readOptionValue('Date')
arguments = str(sys.argv)
user = arguments[1]
resumeType = arguments[2]
version = arguments[3]
style = arguments[4]
fileName = user
fullFileName = user+'/'+resumeType+'/'+version+'/'+style+'/'+fileName

f = open(fullFileName+'.temp')
file =  f.read()
iterations= file.count('#')/2
i=0
while i < iterations:
	first = file.find('#')
	second = file.find('#',first+1)
	option= file[first+1:second]
	replace= readOptionValue(fullFileName,option)
	file = file[:first]+replace+file[second+1:]
	i=i+1

f.close()
os.chdir('poc')
#print getoutput('ls -l')
f = open('hello.tex','w')
f.write(file)
f.close()
os.system('latexmk -pdf hello.tex') 
