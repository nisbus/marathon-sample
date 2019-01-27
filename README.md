#VOLTA NETWORKS mesos sample

##Summary

This project contains everything you need to spin up a Mesos/Marathon service and provides a RESTful API
to Start/Stop useless processes as well as listing one/all running processes.

##Prerequisites

To run this demo you will need the following installed:
 *  [Docker](https://www.docker.com/get-started) 
 *  [docker-compose](https://docs.docker.com/compose/install/)
 
##Getting started

Clone this repository to your computer
```bash
git clone https://github.com/nisbus/volta_mesos.git
```

After the clone is completed open the directory in a terminal and run the command according to your platform

#### Linux
```bash
make
```

#### Windows
```bash
docker-compose build && docker-compose up
```

You should now be able to open the REST API in a browser at http://localhost:5000  
The Marathon UI is available at http://localhost:8080




 
 
 
