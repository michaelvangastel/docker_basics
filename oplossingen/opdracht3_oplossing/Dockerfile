# our base image
FROM alpine

# Install python and pip
RUN apk add python2 --no-cache

# install Python modules needed by the Python app
WORKDIR /usr/src/app/

# copy files required for the app to run
COPY app.py .

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "./app.py"]
