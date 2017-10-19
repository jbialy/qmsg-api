# use a slim version of python 2.7
FROM python:2.7.14-alpine

# set the dir where our app will be coped to
WORKDIR /usr/src/app
# copy the source to image
COPY . .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# launch the app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD [ "app_docker.py" ]