# -*- coding: utf-8 -*-
#  This program is free ; you can redistribute it and/or modify
#  This program is created for study purpose and distributed in the hope that it will be useful
#  but WITHOUT ANY WARRANTY;

#  Author details
#  Gaurav Jadhav

import pprint
import boto3,sys,argparse,re
__version__= '0.0.1'

'''
Get's server name , instance id ,  PublicIpAddress , PrivateIpAddress
Create Tags
Create AMI , assign tag together to AMI and Snapshot
'''
def process(name,tickiet_id,region):

    client = boto3.client('ec2',region)

    if reboot == False:
        print ("Server will reboot [AMI  creation] ")
    else:
        print("Server will not get rebooted while creating AMI ")

    response = client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [name]}])
    print("Server Name: ",name)

    #Get instance_id
    try:
        instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
    except Exception as e:
        print("Exception occoured while looking fot instance kindly check Instance: ERROR :",e)
    print("InstanceId is: ",instance_id)

    #PublicIpAddress
    PublicIpAddress = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    print("PublicIpAddress is: ",PublicIpAddress)

    #PrivateIpAddress
    PrivateIpAddress = response['Reservations'][0]['Instances'][0]['PrivateIpAddress']
    print("PrivateIpAddress is: ",PrivateIpAddress)

    #combination of name and tickit id
    name =  name+'_'+tickiet_id

    #Create ami
    try:
        create_image = client.create_image(InstanceId=instance_id, Name=name, NoReboot=reboot,
    Description='Testing script',

        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                         'Key': 'Name',
                            'Value': name
                    },
                        ]

            },

        ],
        )
        image_id = create_image.get('ImageId')
        print("AMI has been created successfully! ",image_id)
    except Exception as e:
        print("Exception occoured while creating AMI : ERROR :",e)
        sys.exit("Exiting Bye...")

    if not image_id:
        sys.exit("No Image Id Found Exiting Bye ..:)")

    ami_tag = client.create_tags(Resources=[image_id], Tags=[{'Key':'Name', 'Value':name}])


if  __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Enter Instance Name.", default="aws-instance-name")
    parser.add_argument("-t", "--tid", help="Enter your Tickiet ID.")
    parser.add_argument('-r',help='Plase provide Region ')
    parser.add_argument('-reboot',help='No Reboot ',default=True)

    #parser.add_argument("-name", help="echo the string you use here")
    sys.stdout.write('AWS- AMI Automation -by %s Version: <%s>\n\n' % ('Gaurav Jadhav', __version__))

    args = parser.parse_args()
    name = args.name
    tickiet_id = args.tid
    region=args.r
    reboot= args.reboot
    if reboot == "yes":
        reboot= False

    #calling process function
    process(name,tickiet_id,region)