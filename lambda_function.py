import os
import boto3
import pickle
import gspread
import datetime

GOOGLE_CREDENTIALS = 'google_credentials.json'

def write_pickle(data, filename, protocol=pickle.HIGHEST_PROTOCOL):

    with open(filename, 'wb') as file:
        pickle.dump(data, file, protocol=protocol)

def download_sheet(sheet_title, credentials):

    data = {}
    gc = gspread.service_account(credentials)
    sheet = gc.open(sheet_title)
    for wsh in sheet.worksheets():
        data[wsh.title] = wsh.get_all_records()

    return data

def save_to_s3(bucket, local_filename, bucket_filename):

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket.upload_file(local_filename, bucket_filename)

def lambda_handler(event, context):

    sheet_title = os.environ.get('SHEET_TITLE')
    bucket_name = os.environ.get('S3_BUCKET')
    bucket_filename = '{}/{}.pickle'.format(sheet_title, datetime.datetime.now())
    local_filename = '/tmp/data.pickle'
    data = download_sheet(sheet_title, GOOGLE_CREDENTIALS)
    write_pickle(data, local_filename)
    save_to_s3(bucket_name, local_filename, bucket_filename)
