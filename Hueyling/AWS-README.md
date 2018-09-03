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


### After you log in to the EC2 instance. #######

sudo apt-get update
sudo apt-get install python-pip
sudo apt-get upgrade

### install mysql root::mysql ####
sudo apt-get mysql-client mysql-server   

### install apache2 wsgi ####
sudo apt-get install apache2 
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod wsgi
sudo apt-get install git

### install flask and python sql ####
sudo pip install Flask
sudo pip install wtforms
sudo pip install passlib

sudo apt-get install php7.0-fpm php7.0-mysql;
sudo apt-get install sqlite3

### install flask upload and dropzone (This function doesn't seem work with AWS)###
pip install flask-uploads flask-dropzone  

### Install lxml ###
sudo apt-get install python-lxml
sudo apt-get install python3-lxml
sudo apt-get install libxml2-dev libxslt-dev python-dev

### install nltk ###
sudo pip install -U nltk


### Map a app folder to www ######
sudo ln -sT ~/FlaskApp /var/www/html/FlaskApp

### Change the default site enabled under the default conf file and restart apache ######
sudo vim /etc/apache2/sites-enabled/000-default.conf 
sudo /etc/init.d/apache2 restart

### sudo apt install x11-apps ###
sudo apt install x11-apps
xeyes

### Modify static/graph.js to the new ip address ###
var URL_BASE = "http://18.222.230.106";

### This is how you mount the server and log into the aws server #######
ssh -Y -i ./dev.pem ubuntu@18.222.230.106

sshfs -o IdentityFile=/Users/hueyling/GitTutorial/flask-aws/deploy-aws/dev.pem  ubuntu@18.222.230.106:/home/ubuntu /Users/hueyling/AWS -ovolname=AWS



