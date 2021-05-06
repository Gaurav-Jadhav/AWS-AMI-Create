Automate AMI Creation for Customized EC2 Instances #python

You can automate AMI Creation using simple parameters like Server Host Name & Tickit ID (or any id -you can customize it as per your need)
It is easy to use script for system admins , developers or person with basic AWS knowledge.
You can also provide reboot parameter in case you want to reboot server before AMI creation.


How to use script:

  python3 aws_ami.py -n gaurav.jadhav.com -t 1515 -r ap-south-1
