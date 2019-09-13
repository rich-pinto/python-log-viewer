# python-log-viewer
Logfile viewing for inputted log filename


## Prerequisites

* Python 2.7
* Flask, subprocess, time, os, sys Python Modules
* Web Browser
* No existing service listening on TCP port 5020 on the host which will be used to run the log viewer.

## Installation and Setup

* Before installation ensure you have python 2.7 interpretor setup. Flask module must be present or use pip to install it. Ensure that modules like subprocess, os, sys, time are present as well(you should have these once the interpretor is installed).

* Make sure no servcice/process is running on TCP 5020 
```
netstat -tulpn | grep 5020
```

* Clone the github repository
```
git clone <repo url>
```

* Get into the git repo locally and run the python app

> foreground
  ```
  python app.py
  ```
  
> background as a daemon
  ``` 
  nohup python app.py &
  ```
  
* Open a browser and hit the following url
```
http://localhost:5020
```

* Enter the full path of the logfile(filename should be part of the path) and hit submit. You should now be able to see logs in this logfile.

* Refresh the page to view new incoming logs.
  
  
## Running the app in a Docker container

* Ensure that you have the docker engine running on the machine where you're going to run this docker container. On ubuntu, you can run the following command to install docker

``` 
apt install docker.io
```

* Clone the git repo as shown above


* cd into the cloned repo dir and build the image locally

```
docker build -t python-log-viewer:latest .
```

* Run the docker container from the created image

```
docker run -d -p 5020:5020 python-log-viewer
```

* Access the application in a browser, enter the logfile path and Voila!
```
http://<host_ip>:5020
```

