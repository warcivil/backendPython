# pull official base image
FROM python:3.8

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt ./
# --no-cache-dir
RUN pip install  -r requirements.txt
RUN pip3 install requests==2.25.1
COPY . .

# CMD [ "python", "./web_app.py" ]
