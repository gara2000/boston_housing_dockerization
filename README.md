# Dockerization for the boston housing price prediction
## Description
This is a flask app, running a boston housing price predictor

## Get Started:
```bash
git clone https://github.com/gara2000/boston_housing_dockerization.git
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
cd app
python3 app.py
```
Make a prediction
```
./make_predict.sh localhost 5000
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
Make a prediction
```bash
./make_predict.sh
```
