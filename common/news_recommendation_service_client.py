import os
import pyjsonrpc
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'configuration'))

from config_parser import config
from sys_log_client import logger

HOST = str(config['news_recommendation']['host'])
PORT = str(config['news_recommendation']['port'])
URL = 'http://' + HOST + ':' + PORT

client = pyjsonrpc.HttpClient(url=URL)

def getPreferenceForUser(userId):
    preference = client.call('getPreferenceForUser', userId)
    logger.debug("Preference list: %s" % str(preference))
    return preference
