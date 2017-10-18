# qmsg-api

A simple API with UI front-end for storing and retrieving posts.

## objectives

* exposes a simple restful api (CRud):
    - [x] list the all messages 
    - [x] submit / post messages
    - [x] retrieve a message and determines if it's a palindrome

* deployed to the Cloud (AWS)
    - [ ] provision a compute instance programatically
    - [ ] reachable via DNS record

Some EXTRAs to implement:

* provides a simple UI
    - [ ] shows a list of messages posted by the users
    - [ ] allow to post new messages
    - [ ] allows to select a given message to see extra details

- [ ] functional and system tests
- [ ] deployable in a container

## method

The application was built using Flask, Flask-restful and SQLAlchemy. Flask provides the base micro-framework while Flask-restful adds API functionality where routes/endpoints can easily be mapped to resources. SQLAlchemy provides SQL abstraction (ORM) making database/table provisioning and interaction easy. There is no need to write SQL queries, tables are respresented as objects! SQLite database was chosing for demontration purposes, it's local, portable and doesn't require an additional service.

## installation

In order to setup the dependencies and test the application locally you will need the following:

* Python 2.7 (on OSX you can use "brew install python2" for the latest version)
* Install virtualenv globally
```bash
pip2 install virtualenv
```
* Clone the repo:
```bash
git clone https://github.com/jbialy/qmsg-api.git
```
* Create venv and active it:
```bash
cd qmsg-api
vitualenv venv
. venv/bin/activate
```
* Install dependencies:
```bash
pip2 install -r requirements.txt
```
* Develop, tinker and run the app :)

### testing locally

* cd into the working directory
* make sure you've activate your virtualenv (see installation)
* run "python2 run.py" (this assums python binary installed through "brew")
* the server is now listening on http://localhost:5000
> note that if the database doesn't exist it will be provisioned automatically using the schema defined in api/models.py

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

## things to cleanup/make better
* flask-resful handles many errors and provides parsing out of the box but additional error handling should be added

