# qmsg-api

A simple API with UI front-end for storing and retrieving posts.

## objectives

* exploses a simple restful api (CRUD):
    * list the all messages 
    * submit / post messages
    * retrieve a message and determines if it's a palindrome

* deployed to the Cloud (AWS)
    * provision a compute instance programatically
    * reachable via DNS record

Some EXTRAs to implement:

* provides a simple UI
    * shows a list of messages posted by the users
    * allow to post new messages
    * allows to select a given message to see extra details

* functional and system tests
* deployable in a container

## installation

In order to setup the dependencies and test the application locally you will need the following:

* Python 2.7 (on OSX you can use brew install python2 for the latest version)
* Install virtualenv globally (pip2 install virtualenv)
* Clone the repo (git clone git@github.com:jbialy/qmsg-api.git) and with to the working dir
* Create venv (vitualenv venv) and active it (. venv/bin/activate)
* Install dependencies (pip2 install -r requirements.txt)
* Develop, test and run the app :)

### testing locally

* cd into the working directory
* make sure you've activate your virtualenv (see installation)
* run "python2 run.py" (this assums python binary installed through "brew")
* access via http://localhost:5000

### interaction

* let's add a few posts:
```bash
curl -X POST -d "user_id=2&message=how about that?" http://localhost:5000/posts
curl -X POST -d "user_id=2&message=make another post" http://localhost:5000/posts
curl -X POST -d "user_id=5&message=how about a post from user 5?" http://localhost:5000/posts
```
> note that since there is no associated user table, the user_id's are arbitratry and have no relation to an actual user. This is for demontration only!

* display all posts:
```bash
curl http://localhost:5000/posts
```

* display a particular post using post_id:
```bash
curl http://localhost:5000/post/2
```
