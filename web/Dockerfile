# grab python3 and the subjacent OS
FROM python:3
# inside this machine i want my working directory to be: /usr/src/app
WORKDIR /usr/src/app
# copy the requirements.txt file to the current working directory
COPY requirements.txt .
# install the requirements without caching
RUN pip install --no-cache-dir -r requirements.txt
# copy the files of my machine into my working directory
COPY . .
# run the command
CMD ["python", "app.py"]