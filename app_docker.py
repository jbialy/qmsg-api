# app_docker.py

# - for docker we want to bind to all network interfaces
# 

from api import application

if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0')