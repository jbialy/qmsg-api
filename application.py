# application.py

# - file required by AWS ElasticBean that finds the qmsg-api and starts it
# - this is used when as part of the package when provisioning to EB

from api import application

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=False)