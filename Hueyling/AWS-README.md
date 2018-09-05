### Set up AWS ###

This is the website I follow for the aws/apache/wsgi part. It is very clear to read.
https://ketakirk.wordpress.com/deploy-an-app-on-aws/

General steps:

1. Sign-up to AWS
2. Create a IAM user
3. Create a key pair
4. Configure a security group
5. Create an ELB
6. Launch an EC2 instance
7. Connect to EC2 instance via SSH (and configure Apache, Python and Flask)
8. Pull your code from Github
9. Check the path in the wsgi file
10. Enable mod_wsgi

### This is how you log into your aws server #######
ssh -Y -i ./dev.pem ubuntu@18.222.230.106

### After you log in to the EC2 instance. #######

sudo apt-get update
sudo apt-get install python-pip
sudo apt-get upgrade

### install apache2 wsgi ####
sudo apt-get install apache2 
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod wsgi
sudo apt-get install git

### install flask and python sql ####
sudo pip install Flask
sudo pip install wtforms
sudo pip install passlib

sudo apt-get install sqlite3

### Map a app folder to www ######
git clone https://github.com/hlk217/capstone
sudo mv ~/capstone/Hueyling/000-default.conf /etc/apache2/sites-enabled/000-default.conf
sudo mv ~/capstone/Hueyling/FlaskApp ~/
sudo ln -sT ~/FlaskApp /var/www/html/FlaskApp

### Change the default site enabled under the default conf file and restart apache ######
sudo vim /etc/apache2/sites-enabled/000-default.conf 
sudo /etc/init.d/apache2 restart

### Now if you go to your AWS site , You should be able to see Hello World Flask !! #####








### This code will work on Mac to mount the AWS as external drive###
sshfs -o IdentityFile=/Users/hueyling/GitTutorial/flask-aws/deploy-aws/dev.pem  ubuntu@18.222.230.106:/home/ubuntu /Users/hueyling/AWS -ovolname=AWS



#######################   #Below are attempting but aren't successful yet  #######################


### install mysql root::mysql (Didn't use it for now.) ####
sudo apt-get mysql-client mysql-server
sudo apt-get install php7.0-fpm php7.0-mysql;

### install flask upload and dropzone (This function doesn't seem work with AWS)###
pip install flask-uploads flask-dropzone  

### Install lxml (Didn't use it for now) ###
sudo apt-get install python-lxml
sudo apt-get install python3-lxml
sudo apt-get install libxml2-dev libxslt-dev python-dev

### install nltk (attempting to use NLP. Have some issues with AWS)###
sudo pip install -U nltk


### sudo apt install x11-apps ###
sudo apt install x11-apps
xeyes

### (Personal reminder) Modify static/graph.js to the new ip address ###
var URL_BASE = "http://18.222.230.106";

### This is how you mount the server and log into the aws server #######
ssh -Y -i ./dev.pem ubuntu@18.222.230.106

sshfs -o IdentityFile=/Users/hueyling/GitTutorial/flask-aws/deploy-aws/dev.pem  ubuntu@18.222.230.106:/home/ubuntu /Users/hueyling/AWS -ovolname=AWS



