# APM Agent extension

Adds a container with an **example** flask app which uses APM traces and forwards it to the APM
server. 

APM AGENT routes and traces:

```
localhost:11000 - connects to redis and gets a value
localhost:11000/span - custom span which waits to seconds before reply
```

Documentation about each APM agent resource is found:
https://www.elastic.co/guide/en/apm/agent/index.html

## Usage

If you want to include the APM server, run Docker compose from the root of 
the repository with an additional command line arguments referencing the `apm-server-compose.yml` and `apm-agent-compose.yml` file:
                                                                           
```bash
$ docker-compose -f docker-compose.yml -f extensions/apm-server/apm-server-compose.yml -f extensions/apm-agent/apm-agent-compose.yml up
```