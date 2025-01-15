#!/Library/Frameworks/Python.fcamewock/Versions/3.9/bin/python3

from logging import error 
import boto3
import csv 
import time 
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_arguent('--region', action="store",dest='region' , default='us-east-1')
parser.add_arguent('--account', action="store",dest='region' , default='awstest')
args = parser.parser_args()

# initialize boto3 client
ec2 = boto3.client('ec2', region_name=args.region)

#initialize variables
csv_file = args.account + '_tag_failed_Instances.csv'
result=[]


# function to describe the instances and create an array of lists with instance reaper information which can be exported to csv
def add_failed_ids_to_csv(instance_to_be_exported): I
try:
    instances = ec2.describe_instances(InstanceIds=instance_to_be_exported)
    for reservation in instances[ 'Reservations']: 
        for instance in reservation[ 'Instances']:
            reaper_tag_value = "off"
            for tag in instance[ 'Tags']: 
                if tag[ 'Key'] =='Name' :
                    instance_name=tag[ 'Value' ]
                if tag[ 'Key'] =='reaper:maintenance':
                    reaper_tag_value=tag[ 'Value']
            if reaper_tag_value != "on":
                result. append({
                    'Name': instance_name,
                    ' Instance Id': instance["Instanceld"],
                    'InstanceState': instance[ 'State'] ['Name'],
                    ' ReaperMaintenanceTag': reaper_tag_value,
                    'Private IP': instance.get("PrivatelpAddress", 'NA')
               })
except Exception as e:
        print("** Export instances : Error describing instances")
        print (e)