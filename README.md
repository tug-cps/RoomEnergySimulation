# default_model_environment

# Environment repo
- single environment definition that we use as basis for ALL models
- standalone repo just for conda and venv definitions
- include sample docker
- tag releases on this repo

- conda
- venv
- pyenv
- docker
- pip wheel of 'common' utils

# Model repos
- all new models start with a fork of this environment repo
- all models that are finally deployed have to have:
	- csv training data
	- training script
	- produced model as pickel
	- a python file with a "predict" function that pulls the needed data from dbs, perform preprocessing, feature generation, calls the pickeled model, and writes the predictions back to db
	- a json file describing the scheduling of the model
	- has to be tagged with version as released model if it is deployed

# Predictor service
- docker container with a simple script that executes model scripts at a certain location
- call sequentially in order to avoid having all models run at the same time
- uses the scheduling json from each model to decide which models to be called
- new models can be added by simply putting the script in this location and the corresponding pickle file
- models can be deactivated by deleting them
