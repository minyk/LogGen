'''
Created on Jul 27, 2011

@author: bitaholic
'''
from os import mkdir
from os.path import join, exists
import Config
import ConfigParser
import datetime
import sched
import string
import sys
import time

logTemplate = ''
reqTemplate = ''
logId = 0
logNum = 0
logCountInMinute = Config.LOG_COUNT_IN_MINUTE
delay = Config.DELAY
outputDir = Config.OUTPUT_DIR

s = sched.scheduler(time.time, time.sleep)

def main():
    global logCountInMinute, delay, outputDir
    
    if len(sys.argv) == 2:
        logCountInMinute = int(sys.argv[1])
    if len(sys.argv) == 3:
        delay = int(sys.argv[2])
    if len(sys.argv) == 4:
        outputDir = sys.argv[3]
        
    loadconfig()
    startGenLog()

def loadconfig():
    global logTemplate
    config = ConfigParser.ConfigParser()
    config.read(Config.CONF_FILE)
    logTemplate = config.get('Common', 'LogTemplate')
    
def startGenLog():
    s.enter(delay, 1, genLog, ())
    print 'start to generate logs (every ' + str(delay) + 's)'
    s.run()
    print 'finished to generate logs (total count : ' + logNum 

def genLog():
    global logNum
    loadTemplate()
    body = ''
    for i in range(logCountInMinute):
        body = body + (reqTemplate.substitute({'txid':logNum, 'timestamp':time.strftime('%X %x %Z')}) + '\n')
        logNum += 1; 
    
    saveFile(body)
    s.enter(delay, 1, genLog, ())
    
def saveFile(body):
    prefix = 'req_'
    filename = prefix + datetime.datetime.today().isoformat()
    if not exists(outputDir):
        mkdir(outputDir)
        
    print 'created ', join(outputDir, filename)
    logfile = open(join(outputDir,filename), 'w')
    logfile.write(body)
    logfile.flush()
    logfile.close()
    
def loadTemplate():
    global reqTemplate
    file = open(join(Config.RESOURCE_DIR, logTemplate))
    reqTemplate = string.Template(file.read())
    file.close()
    
if __name__ == '__main__':
    main()