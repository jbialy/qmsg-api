# application.py

# - file required by AWS ElasticBean that finds the qmsg-api and starts it
# - this is used when as part of the package when provisioning to EB

from api import app

if __name__ == '__main__':
    app.run(debug=False)