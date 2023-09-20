import asyncio as asy
from pathlib import Path
import boto3 as aws
import json as js
import shutil as sh
import hashlib as hl
import requests as rq
import datetime as dt
import time as tm
from botocore.config import Config
import os, sys


#global variables
TODAY = dt.datetime.now() + dt.timedelta(days=1) #today
DELTA = 5 # retroactive events DELTA DAYS
BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #get the path of the file
ACCOUNT_ID = [] #account id
REGIONS = [] #list of regions


#setup the environment
def create_folder():
    try:    
        print("Creating folder...")
        global BASE_PATH, ACCOUNT_ID
        ACCOUNT_ID = aws.client('sts').get_caller_identity().get('Account')
        #if exists deldefete
        if os.path.exists(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}'.format(ACCOUNT_ID))):
            sh.rmtree(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}'.format(ACCOUNT_ID)))
        #create folder
        os.mkdir(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}'.format(ACCOUNT_ID)))
        
    except Exception as e:
        print("Error: {}".format(e))

def get_regions():
    try:
        print("Getting regions...")
        global REGIONS
        REGIONS = aws.client('ec2').describe_regions()['Regions']
        REGIONS = [x['RegionName'] for x in REGIONS]    
    except Exception as e:
        print("Error: {}".format(e))

#download the cloudtrail files
def download_cloudtrail():
    #for each region download the cloudtrail files day by day
    global TODAY, DELTA, BASE_PATH, ACCOUNT_ID, REGIONS
    for region in REGIONS:
        #create a folder for the region
        os.mkdir(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}/{}'.format(ACCOUNT_ID, region)))
        print("Downloading region {}...".format(region))
        #get the cloudtrail client
        client = aws.client('cloudtrail', region_name=region)
        #get the start date
        start_date = TODAY - dt.timedelta(days=DELTA)
        #get the end date
        end_date = TODAY
        try:
            #while the start date is less than the end date
            while start_date < end_date:
                #get the day
                day = start_date.strftime('%Y-%m-%d')
                print("Downloading {}...".format(day))
                # paginate the search using start time and end time
                paginator = client.get_paginator('lookup_events')
                page_iterator = paginator.paginate(
                    StartTime=start_date,
                    EndTime=end_date
                )
                #for each page
                for page in page_iterator:
                    #get the events
                    events = page['Events']
                    #if there is events
                    if events:
                        #save the events in a file
                        with open(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}'.format(ACCOUNT_ID), region, '{}.json'.format(day)), 'a') as file:
                            file.write(js.dumps(events, indent=4, default=str))

                #increment the start date
                start_date += dt.timedelta(days=1)

        except Exception as e:
            print("Error: {}".format(e))

#zip the files into a single tar.gz file
def zip_files():
    import tarfile
    try:
        print("Zipping files...")
        global BASE_PATH, ACCOUNT_ID
        #get the files
        files = os.listdir(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}'.format(ACCOUNT_ID)))
        #zip the files
        with tarfile.open(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}.tar.gz'.format(ACCOUNT_ID)), 'w:gz') as tar:
            for file in files:
                tar.add(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}/{}'.format(ACCOUNT_ID, file)), arcname=file)
    except Exception as e:
        print("Error: {}".format(e))

#hash the zip file
def hash_zip():
    try:
        print("Hashing zip file...")
        global BASE_PATH, ACCOUNT_ID
        #get the hash md5 and sha 1 and sha 256
        md5 = hl.md5()
        sha1 = hl.sha1()
        sha256 = hl.sha256()
        #open the file
        with open(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}.tar.gz'.format(ACCOUNT_ID)), 'rb') as file:
            #update the hash
            md5.update(file.read())
            sha1.update(file.read())
            sha256.update(file.read())
        #save the hash in the .hash file
        with open(os.path.join(BASE_PATH, 'CloudTrail-Dump_{}.tar.gz.hash'.format(ACCOUNT_ID)), 'w') as file:
            file.write('MD5: {}\n'.format(md5.hexdigest()))
            file.write('SHA1: {}\n'.format(sha1.hexdigest()))
            file.write('SHA256: {}\n'.format(sha256.hexdigest()))
    except Exception as e:
        print("Error: {}".format(e))


def main():
    global TIME 

    #start the time
    TIME = tm.time()

    #create the folder
    create_folder()

    #get the regions
    get_regions()

    #download the cloudtrail files
    download_cloudtrail()

    #zip the files
    zip_files()

    #hash the zip file
    hash_zip()

    #end the time
    TIME = tm.time() - TIME     
    print("Time: {} seconds".format(TIME))

#verificar CT com CT-Digest

if __name__ == '__main__':
    main()
    