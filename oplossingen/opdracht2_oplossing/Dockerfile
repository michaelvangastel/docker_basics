# our base image
FROM alpine

# Install python and pip
RUN apk add --no-cache py-pip

# install Python modules needed by the Python app
WORKDIR /usr/src/app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

# copy files required for the app to run
COPY app.py .
COPY templates/index.html ./templates/

ENV TEXT_COLOR white
ENV NAME world

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python3", "./app.py"]
