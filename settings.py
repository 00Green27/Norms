import os
from configobj import ConfigObj
from datetime import datetime

config = ConfigObj("norm.conf")

DATABASE_FILENAME = "norm.db"
IS_OPEN_REPORT = config['general']['open_report']
DATABASE_PATH = os.path.abspath(config['paths']['database'])
BACKUP_PATH = os.path.abspath(config['paths']['backup'])
TEMPLATES_PATH = os.path.abspath(config['paths']['templates'])
REPORT_PATH = os.path.abspath(config['paths']['reports'])
YEAR = datetime.now().year

#def setProperty(prop, value, section="general"):
#    config[section][prop] = value

#def getProperty(prop, section="general"):
#    return config[section][prop]

#def getPathProperty(prop):
#    return os.path.abspath(config["paths"][prop])

#def load():
#    open_report = config['general']['open_report']
#    database_path = os.path.abspath(config['paths']['database'])
#    backup_path = os.path.abspath(os.path.dirname(config['paths']['backup']))
#    templates_path = os.path.dirname(config['paths']['templates'])
#    report_path = os.path.abspath(os.path.dirname(config['paths']['reports']))

def save():
    config.write()

if __name__ == '__main__':
    print getProperty("database", "paths")
    save()