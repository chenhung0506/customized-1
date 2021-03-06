# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')  
dotenv_path = os.path.join(APP_ROOT, '../docker/dev.env')
load_dotenv(dotenv_path)
print( os.getenv('IS_LOADED') + ", .env file path: " + dotenv_path )

PORT=os.environ.get('PORT', os.getenv('PORT'))
LOG_LEVEL=os.environ.get('LOG_LEVEL', os.getenv('LOG_LEVEL'))
TIME_DURATION=os.environ.get('TIME_DURATION', os.getenv('TIME_DURATION'))
START_TIME=os.environ.get('START_TIME', os.getenv('START_TIME'))
END_TIME=os.environ.get('END_TIME', os.getenv('END_TIME'))
CALL_DIRECTION=os.environ.get('CALL_DIRECTION', os.getenv('CALL_DIRECTION'))
PHONE_NUMBER=os.environ.get('PHONE_NUMBER', os.getenv('PHONE_NUMBER'))
FREQUENCE=os.environ.get('FREQUENCE', os.getenv('FREQUENCE'))
PAGE_SIZE=os.environ.get('PAGE_SIZE', os.getenv('PAGE_SIZE'))
ARMS_API=os.environ.get('ARMS_API', os.getenv('ARMS_API'))
GET_TAG_API=os.environ.get('GET_TAG_API', os.getenv('GET_TAG_API'))
GET_ASR_RESULT_API=os.environ.get('GET_ASR_RESULT_API', os.getenv('GET_ASR_RESULT_API'))
GET_TAG_API_SLEEP_TIME=os.environ.get('GET_TAG_API_SLEEP_TIME', os.getenv('GET_TAG_API_SLEEP_TIME'))
ENTERPRISE=os.environ.get('ENTERPRISE', os.getenv('ENTERPRISE'))
USER_ID=os.environ.get('USER_ID', os.getenv('USER_ID'))
TRANSMIT_CRON=os.environ.get('TRANSMIT_CRON', os.getenv('TRANSMIT_CRON'))
LOG_FOLDER_PATH=os.environ.get('LOG_FOLDER_PATH', os.getenv('LOG_FOLDER_PATH'))
SERVER_IP=os.environ.get('SERVER_IP', os.getenv('SERVER_IP'))