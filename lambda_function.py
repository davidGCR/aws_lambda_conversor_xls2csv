import json
import os
import glob
import sys
sys.path.append('libs')
# o = win32com.client.Dispatch("Excel.Application")
# o.Visible = False
# input_dir = r"C:\Users\ZAT02\Downloads\MKF-CUOTAS_GESTIONADAS\landing-SAR"
# output_dir = r"C:\Users\ZAT02\Downloads\MKF-CUOTAS_GESTIONADAS\landing-SAR\xlsx"
# files = glob.glob(input_dir + "/*.xls")
# print(files)

import boto3
from xlwt import Workbook
import io

def fix_corrupt_xls(bucket_name, input_file, output_file):
    # bucket_name = "auna-dlaqa-raw-s3"
    # input_file = "structured-data/OLAP/dwh-gestionsalud/pry-gs-marketforceintermedio/xls_sar_prd/SAR-UG-19012023.xls"
    # output_file = "structured-data/OLAP/dwh-gestionsalud/pry-gs-marketforceintermedio/xls_sar_prd/test3.xls"
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    object = bucket.Object(input_file)
    data = object.get().get('Body').read()
    # Convert to a "unicode" object
    text_obj = data.decode('UTF-16')  # Or use the encoding you expect
    # Use text_obj how you see fit!
    data = io.StringIO(text_obj)
    xldoc = Workbook()
    # Adding a sheet to the workbook object
    sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
    # Iterating and saving the data to sheet
    for i, row in enumerate(data):
        # print(row)
        # Two things are done here
        # Removeing the '\n' which comes while reading the file using io.open
        # Getting the values after splitting using '\t'
        for j, val in enumerate(row.replace('\n', '').split('\t')):
            sheet.write(i, j, val)
    buffer = io.BytesIO() 
    xldoc.save(buffer)
    # Put object to S3
    s3_resource = boto3.resource('s3')
    response = s3_resource.Object(bucket_name, output_file).put(Body=buffer.getvalue())
    return response

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    input_file = event['input_file']
    output_file = event['output_file']
    response = fix_corrupt_xls(bucket_name=bucket_name, input_file=input_file, output_file=output_file)
    return {
        'statusCode': 200,
        'body': {
            "msj": "testing my lambda22222333332!!!",
            "objects": json.dumps(
                {
                    "bucket_name": event['bucket_name'],
                    "input_file": event['input_file'],
                    "output_file": event['output_file'],
                    "response_status": response['ResponseMetadata']['HTTPStatusCode']
                })
        }
    }