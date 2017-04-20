#!/usr/bin/python3

from scgb.main import bot_init, check_comments
from scgb.database import Database

import imp
import os
import sys
import logging

def load_config():
    # Init config
    if len(sys.argv) > 1:
        config = imp.load_source('scgb_config', sys.argv[1])
    elif os.path.exists('config.py'):
        config = imp.load_source('scgb_config', os.path.join(os.getcwd(), 'config.py'))
    else:
        logging.critical('Please, rename config.py.template to config.py and edit it.\nOr specify a config to load on the command line: py scgb.py <config file>')
        sys.exit(1)

    # Init config defaults to simplify mass configuration
    try:
        defaults = imp.load_source('scgb_defaults', os.path.join(os.getcwd(), 'defaults.py'))
    except ImportError:
        pass
    else:
        for key in defaults.defaults.keys():
            if not hasattr(config, key):
                setattr(config, key, defaults[key])
        
    return config
    
if __name__ == '__main__':
    # Init log
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, datefmt='[%Y-%m-%d %H:%M:%S]', format='%(asctime)s %(levelname)s %(message)s')
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
	
	# Init config
    config = load_config()
			
    # Init database
    db = Database(config.stats_database)
            
    bot_init(config)
    check_comments()
