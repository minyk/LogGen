from os.path import dirname
import sys
import ConfigParser

basedir = dirname(sys.modules[__name__].__file__)
print basedir

config = ConfigParser.ConfigParser()
print config
config.read('../config/config.cfg')
if config.has_option('Common', 'OutputDir'):
    print config.get('Common', 'OutputDir')
else:
    print 'no config'
