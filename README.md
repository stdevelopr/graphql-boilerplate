## GraphQL API boilerplate

This project has two folders:

- web folder:\
  (contains the files)\
  _app.py_ - wich is responsible to run the app\
  _requirements.txt_- the requiremtns to run the code\
  _Dockerfile_ - explains how to run the web module

- db folder
  (contains the files)\
  _Dockerfile_ - explains how to run the database

At the top level the file docker-compose.yml is responsible to start the aplication and control the comunications between the service modules

### To run the application:

`sudo docker-compose build`\
`sudo docker-compose up`
