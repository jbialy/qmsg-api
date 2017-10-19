# qmsg-api

A simple API with UI front-end for storing and retrieving posts.

## objectives

* exposes a simple restful api (CRud):
    - [x] list the all messages 
    - [x] submit / post messages
    - [x] retrieve a message and determines if it's a palindrome

* deployed to the Cloud (AWS)
    - [x] provision a compute instance programatically
    - [x] reachable via DNS record

Some EXTRAs to implement:

* provides a simple UI
    - [ ] shows a list of messages posted by the users
    - [ ] allow to post new messages
    - [ ] allows to select a given message to see extra details

- [ ] functional and system tests
- [x] deployable in a container

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
curl -X POST -d "user_id=2&message=how about that?" http://localhost:5000/post
curl -X POST -d "user_id=2&message=make another post" http://localhost:5000/post
curl -X POST -d "user_id=5&message=how about a post from user 5?" http://localhost:5000/post
curl -X POST -d "user_id=12&message=nurses run" http://localhost:5000/post
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

## deployment
AWS provides an easy way to deploy flask applications using AWS ElasticBeanstalk. You can deploy this app to AWS using a free tier account and following these steps:

* install "awsebcli" using pip
```bash
pip2 install awsebcli
```
* initialize a new application on AWS. You will need an account with a "service role" and your AWS credentials configured
```bash
eb init --platform "Python 2.7" --region "ca-central-1" qmsg-api 
```
* create your environmenet and bring up all services:
```bash
eb create flask-dev --cname qmsg-api-dev --single
```
* an api instance will be be available using the cname specific. ex: http://qmsg-api-dev.ca-central-1.elasticbeanstalk.com
* when done, the environment and application can be terminated using:
```bash
eb terminate flask-dev
```

### docker ###
You can also run the app in docker by pulling the image directly from dockerhub
```bash
docker pull jbialy/qmsg-api
docker run -d -p 5000:5000 jbialy/qmsg-api
```
The service will be accessible on localhost:5000

Try it with [play-with-docker!](http://labs.play-with-docker.com)

## things to cleanup/make better
* unit testing should be done to make sure that nothing breaks during development. This can be implemented using the "request" module and have a script run a set of requests to test the integrity of the api.
* some of the resource logic could be moved to the db.Model object to clean up the code
* custom 404 page could be created to provide better response

## references
* [Flask](http://flask.pocoo.org)
* [Flask-restful](http://flask-restless.readthedocs.io/en/stable/)
* [SQLAlchemy](https://www.sqlalchemy.org)
* [Flask on AWS using EB](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)