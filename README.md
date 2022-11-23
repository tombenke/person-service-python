# person-service-python
[![Quality Check Status](https://github.com/tombenke/person-service-python/workflows/Quality%20Check/badge.svg)](https://github.com/tombenke/person-service-python)
[![Release Status](https://github.com/tombenke/person-service-python/workflows/Release/badge.svg)](https://github.com/tombenke/person-service-python)
![Coverage](./coverage.svg)

A sample easer REST API endpoint implementation in Python

## Prerequisites

You will need the following tools installed on your machine:
- bash
- git
- Python 3.9
- sed
- [Task](https://taskfile.dev/)

## Installation

1. clone this repo:

```bash
    git clone git@github.com:tombenke/person-service-python.git
```

2. Step into the newly cloned folder:

```bash
    cd person-service-python
```

3. Create a Python virtual environment in the local folder:

```bash
    task venv-create
```

4. Activate the newly created virtual environment:

```bash
    . venv/bin/activate
```

5. Install the dependencies:

```bash
    task install-dev-editable
```

6. Run tests and docs generation:

```bash
    task
```

7. Build the package, and try to run it:

```bash
    task build
    dist/cli --help
```

## Usage

Start the REST API gateway with the person-rest-api definition (docker-compose.test.yml):

```bash
task dc-up
```

Start the container with service implementations (docker-compose.services.yml):

```bash
task dc-services-up
```

Run the tests against the endpoints:

```bash
./test.sh
```

Or use the endpoints directly:

```bash
curl http://localhost:3007/persons/
```

## Development

Use the tasks are available during the work:

```bash
task list

* build:                      Build a single binary application from the source code
* build-docker:               Build docker image
* clean:                      Clean temporary files and folders
* coverage:                   Test coverage
* dc-down:                    Clean up docker containers
* dc-logs:                    Get all docker container logs
* dc-logsf:                   Get all docker container logs and follow
* dc-services-down:           Clean up services docker containers
* dc-services-up:             Start services  docker containers
* dc-stop:                    Stop docker containers
* dc-up:                      Start docker containers
* dc-upd:                     Start docker containers in the background
* default:                    Executes all the tests then build the binary
* dockerfile-lint:            Run the dockerfile linter
* docs:                       Generate module documentation into the docs/ folder
* format:                     Autoformat the source files
* install:                    Install the package and its dependencies
* install-dev:                Install the package and its dependencies for development
* install-dev-editable:       Install the package and its dependencies for development with editability
* install-git-hooks:          Install git hooks
* lint:                       Run python linter
* pre-commit:                 Runs the QA tasks from a git pre-commit hook
* push-docker:                Push docker image
* test:                       Run all the tests
* test-verbose:               Run all the go tests
* venv-create:                Create a new Python Virtual Environment under the local folder
```

## License
The scripts and documentation in this project are released under the [MIT License](LICENSE)

