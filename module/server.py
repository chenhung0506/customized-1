# -*- coding: utf-8 -*-
from flask import Flask
# from flask_cors import CORS
import log as logpy
import re
import os
import const
import controller
import flask_restful
import utils
from flask_restful import Api
from flask_restful import Resource
from datetime import datetime
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

utils.setLogFileName()
log = logpy.logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)
controller.setup_route(api)

if __name__=="__main__":
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(utils.setLogFileName, CronTrigger.from_crontab('59 23 * * *'))
    # sched.add_job(controller.transmitProcess, CronTrigger.from_crontab(const.TRANSMIT_CRON), [None])
    app.run(host="0.0.0.0", port=const.PORT, debug=True, use_reloader=False)