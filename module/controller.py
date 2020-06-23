# coding=UTF-8
import requests
import json
import time
import re
import ast
import logging
import os
import math
import time
import ctypes 
import threading
from datetime import datetime
from flask import Flask, Response, render_template, request, redirect, jsonify
from threading import Timer,Thread,Event
import dao
import const
from flask_restful import Resource
import log as logpy
import pymysql
import service
import utils
from datetime import datetime

log = logpy.logging.getLogger(__name__)

def setup_route(api):
    api.add_resource(HealthCheck, '/healthCheck')
    api.add_resource(BatchStart, '/batchStart')
    api.add_resource(BatchStop, '/batchStop')
    api.add_resource(Transmit, '/transmit')
    api.add_resource(Test, '/test')
    api.add_resource(TestGetChatRecords, '/testGetChatRecords')

class HealthCheck(Resource):
    log.debug('check health')
    def get(self):
        return {
            'status': 0,
            'message': 'success',
            'method': request.method,
            'username': request.form.get('username'),
            'PHONE_NUMBER': const.PHONE_NUMBER
        }, 200

class BatchStop(Resource):
    def get(self):
        log.info('BatchStop api start')
        return {
            'status': 200,
            'message': utils.stop_batch()
        }, 200

class BatchStart(Resource):
    def get(self):        
        log.info('stop batch:' + utils.stop_batch())
        log.info('BatchStart api start')
        time.sleep(int(5))
        utils.prepare_batch_blocking(transmitProcess,None)
        # utils.prepare_batch_blocking(batchTest,'*/1 * * * *',None)
        
        # sched = BlockingScheduler()
        # sched.add_job(cronTest, CronTrigger.from_crontab(const.TRANSMIT_CRON))
        # sched.start()
        return {
            'message': 'success'
        }, 200

def batchTest():
    log.info(datetime.today().strftime('%Y-%m-%d'))

class TestGetChatRecords(Resource):
    def get(self):
        log.info('TestGetChatRecords api start')
        log.info(testGetChatRecords().text.encode('utf8'))

        return {
            'message': str(testGetChatRecords().text.encode('utf8'))
        }, 200

class Test(Resource):
    def get(self):
        log.info('Test api start')
        return {
            'status': 200,
            'message': transmitProcessTest(request)
        }, 200

class Transmit(Resource):
    def get(self):
        return {
            'status': 200,
            'message': transmitProcess(request)
        }, 200

def transmitProcess(request):
    try:
        callApi=service.CallApi()
        dataForRakutens = callApi.getTag(request)
        dataForRakutens = callApi.sortData(dataForRakutens)
        # return dataForRakutens
        log.info("dataForRakuten quantity:" + str(len(dataForRakutens['data'])))
        report=[]
        errorEmail=""
        for val in dataForRakutens['data']:
            dataForRakuten={}
            dataForRakuten['data']=[]
            dataForRakuten['data'].append(val)
            dataForRakuten['total_size']=1
            # return dataForRakuten
            callArmsResponse=callApi.transmitToArms(dataForRakuten)
            if callArmsResponse.status_code == 204 :
                log.info('Transmit success')
                report.append({"session_id":val["session_id"], "message":"success", "status": 200})
            # elif callArmsResponse.status_code == 400 :
            #     log.info('Transmit fail, status: ' + str(callArmsResponse.status_code) + ', message: ' + callArmsResponse.text)
            #     report.append({"session_id":val["session_id"], "message":callArmsResponse.text, "status": 400})
            else:
                log.info('Transmit fail, status: ' + str(callArmsResponse.status_code) + ', message: ' + callArmsResponse.text)
                resendUrl='http://' + const.SERVER_IP + ':' + const.PORT + '/transmit?phone_number=0277550100&call_direction=outbound&session_id=' + val["session_id"]
                errorEmail = errorEmail + 'transmit error, session id: ' + val["session_id"] + '&nbsp;&nbsp;&nbsp;&nbsp;<a href="' + resendUrl + '"> click here to resend </a><br>'
                report.append({"session_id":val["session_id"], "message":"fail", "status": 204 , "error_data" : dataForRakuten})
        
        
        if errorEmail != "":
            log.info('send error email')
            utils.sendEmail(["chenhung0506@gmail.com", "chenhunglin@emotibot.com"], errorEmail)

        log.info('process complete')

        # raise Exception('test send email')

        return report
        # try:
        #     conn = pymysql.Connect(host='0.0.0.0',user='user',passwd='password',db='db',charset='utf8')
        #     dao.Database(conn).insertTransmit(dataForRakutens)
        # except Exception as e:
        #     log.info("SQL occured some error: "+utils.except_raise(e))
        # finally:
        #     conn.close()

    except Exception as e:
        log.error("transmitProcess error: "+utils.except_raise(e))
        return utils.except_raise(e)

def transmitProcessTest(request):
    try:
        callApi=service.CallApi()
        callArmsResponse=callApi.transmitToArmsTest()
        if callArmsResponse.status_code == 204 :
            log.info('Transmit success')
            return 'success'
        else:
            log.info('Response status: ' + str(callArmsResponse.status_code) + ', message: ' + callArmsResponse.text)
            return 'fail'
        log.info('process complete')

    except Exception as e:
        log.error("transmitProcess error: "+utils.except_raise(e))

def testGetChatRecords():
    try:
        callApi=service.CallApi()
        # s_reponse=callApi.getChatRecords(request).text.encode('utf8')
        # log.info(s_reponse)
        return callApi.getChatRecords("1eb7c32c-9333-11ea-bbff-119443b68c06")
        
    except Exception as e:
        log.error("transmitProcess error: "+utils.except_raise(e))