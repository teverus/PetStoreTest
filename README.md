# PetStore Testing

* [Quick start](#quick-start)
* [Run the tests and get an HTML report](#run-the-tests-and-get-an-html-report)
* [Run the tests in GitLab CI/CD](#run-the-tests-in-gitlab-cicd)
* [Run the tests in a Docker container](#run-the-tests-in-a-docker-container)

## Quick start
_Note: You must have Python 3.6+ installed and operational on your machine._

_Note: If you start the tests for the first time, please do the following:_
```commandline
py -m venv venv && pip install -r requirements
```
To run the tests, navigate to the root of the repository and execute 
```commandline
pytest
```
All options are already set in `pytest.ini`

## Run the tests and get an HTML report
_Note: This will open the report in the default browser._

To run the tests and get an HTML report, navigate to the root of the repository and execute
```commandline
pytest & report.html
```
`report.html` is a self-contained HTML file that can be easily shared.

## Run the tests in GitLab CI/CD
The repository already features a `.gitlab-ci.yml`. You can change it to your liking. 

Clone the repository to GitLab and a CI/CD pipeline will appear automatically.

To access the report, please open a build when it's finished and hit "Browse" on the right.

## Run the tests in a Docker container
_Note: You must have Docker installed and operational on your machine._

The repository already features a `Dockerfile`. You can change it to your liking.

To run the tests in a container, navigate to the root of the repository and execute
```commandline
docker build -t my_image . & docker run -it --rm my_image
```
This will build an image and run it in the console for you to see the results.