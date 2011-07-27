from os.path import dirname, join
import sys
import ConfigParser



BASE_DIR = dirname(sys.modules[__name__].__file__)

CONF_DIR = join(BASE_DIR, '..', 'config')
CONF_FILE = join(CONF_DIR, 'config.cfg')

RESOURCE_DIR = join(BASE_DIR, '..', 'resources')

config = ConfigParser.ConfigParser()
config.read(CONF_FILE)

if config.has_option('Common', 'outputdir'):
    OUTPUT_DIR = config.get('Common', 'outputdir')
else:
    OUTPUT_DIR = '/tmp/loggen'
    
if config.has_option('Common', 'delay'):
    DELAY = int(config.get('Common', 'delay'))
else:
    DELAY = 60
    
if config.has_option('Common', 'log_count_in_minute'):
    LOG_COUNT_IN_MINUTE = int(config.get('Common', 'log_count_in_minute'))
else:
    LOG_COUNT_IN_MINUTE = 6000
    
