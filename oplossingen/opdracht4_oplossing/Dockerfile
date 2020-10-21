# our base image
FROM alpine

# Install python and pip
RUN apk add python3 --no-cache

# install Python modules needed by the Python app
WORKDIR /usr/src/app/

# copy files required for the app to run
COPY app.py .

# run the application
ENTRYPOINT ["python3", "./app.py"]
CMD ["1","4","5"]
