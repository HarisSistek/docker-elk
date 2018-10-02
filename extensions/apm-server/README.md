# APM Server extension

Adds a container for Elasticsearch APM server. Forwards caught errors and traces to Elasticsearch
server that can be viewed in Kibana. 

## Usage

If you want to include the APM server, run Docker compose from the root of 
the repository with an additional command line argument referencing the `apm-server-compose.yml` file:
                                                                           
```bash
$ docker-compose -f docker-compose.yml -f extensions/apm-server/apm-server-compose.yml up
```