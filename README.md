# Basic REST API Testing Framework

Naive solution for a basic REST API testing framework. This framework was designed to interact with the [Basic RestAPI App](https://github.com/jllopez/basic-restapi-app). Make sure you run the `Basic RestAPI App` before setting up this project.

This project is used for educational purposes. It encourages users to enhanced it and adapt it to their needs. The idea is to start with the most simple solution and build on top of it.

The framework was designed to run inside a `Docker` container to strip out the complexity of setting virtual environments, facilitate its distribution and avoid the infamous ***but it works on my machine*** conversation.

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Make](https://discussions.apple.com/thread/1404907)
- [Python 3.7 and up](https://www.python.org/downloads/release/python-370/)

## Setup

1. Open a terminal

2. Change to your favorite local directory (i.e. `cd /opt`)

3. Clone the repository

```bash
git clone git@github.com:jllopez/basic-restapi-testfwk.git
```
4. Change to the project root directory

```bash
cd /opt/basic-restapi-testfwk
```

5. Create a new file, name it `secrets.ini` and add the following contents

```bash
APP_URL=http://host.docker.internal:8080
ADMIN_USER=admin
ADMIN_PASSWORD=admin

```

5. Start development environment

```bash
make dev
```

> This command will remove any existing `restapi_testfwk` containers, build a new `test/restapi_testfwk` image, start a container, mount local code under `/opt/restapi_testfwk` and provide a `/bin/bash` terminal.
