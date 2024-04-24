# Dockerization for the boston housing price prediction
## Description
This repo has two parts:
* It trains a boston housing model and packages it into a container on the GitHub container registry
* It walks you through the process of running an app that predicts the boston housing, locally and using Docker containers

## Getting Started:
```bash
git clone https://github.com/gara2000/boston_housing_dockerization.git
cd boston_housing_dockerization
```
### Run the app locally
Create a virtual environment
```bash
python3 -m venv .mlops
```
Activate the vritual environment
```bash
source .mlops/bin/activate
```
Install dependencies
```bash
make install
```
Run the app
```bash
cd src/app
python3 app.py
```
Make a prediction.
In another terminal run:
```
./make_predict.sh
```

### Run the app with Docker
Build the Docker image
```bash
make docker-build
```
Run the Docker container
```bash
make docker-run
```
Make a prediction.
In another terminal run:
```bash
./make_predict.sh
```

## Pipelines
### Update the model
This repo offers a Continuous Integration pipeline to automatically train the model upon change of the train.py code or the data.csv data file
* Use the ```src/train/train.py``` file to change the training code.
* Use the ```src/train/data.csv``` file to change the data (ensure compatibility between train and test data, and ensure that the last row of the data contains the labels)
* Push to the github repo, this will trigger the .github/workflows/python-train.yml file which will run a CI pipeline, the pipeline does the following:

> Lint the train.py code: this analyzes the train.py code fo find programming errors, bugs, stylistic issues, ...

> Train the model and update the boston_housing_predition.joblib file, and push it to the repo automatically (make sure that the workflow permissions is set to **Read and write**, otherwise the push to the repo will fail)

* Run ```git pull``` to get the updates locally

### Build model container and integrate it on Github registry
* Fork the repository to have your own copy
* Add a secret variable with name GH_REGISTRY, and a value containing a Personal Access Token (PAT) for your account
* Make changes to the repo
* Push the changes to GitHub, this will trigger the .github/workflows/main.yml pipeline, which will build the container image and push it to Github registry
* To pull the container image you should first login to the docker registry with
```bash
echo $PAT | docker login ghcr.io --username <github-username> --password-stdin
```
where $PAT is an environment variable containing your Personal Access Token
* Then pull the image with
```bash
docker pull ghcr.io/<gihub-username>/boston_housing:latest
```