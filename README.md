Automate AMI Creation for Customized EC2 Instances #python #boto3

You can automate AMI Creation using simple parameters like Server Host Name ,Region , Tickit ID (or any id -you can customize it as per your need)
It is easy to use script for system admins , developers or person with basic AWS knowledge.
You can also provide reboot parameter in case you want to reboot server before AMI creation.

Git Clone:

    https://github.com/Gaurav-Jadhav/AWS-AMI-Create.git
    cd AWS-AMI-Create

Installations:

    pip install boto3
    

After installing boto3
Next, set up credentials (in e.g. ~/.aws/credentials):

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ~/.aws/config):

    [default]
    region=us-east-1

Arguments:

    parser.add_argument("-n", "--name", help="Enter Instance Name.", default="aws-instance-name")
    parser.add_argument("-t", "--tid", help="Enter your Tickiet ID.")
    parser.add_argument('-r',help='Plase provide Region ')
    parser.add_argument('-reboot',help='No Reboot ',default=True)


Usage:

    python3 aws_ami.py -n hostname.com -t tickitid -r ap-south-1
