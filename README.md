## Research Code ➙ Production Code ➙ Deployment

### Project Structure

```
end-to-end-ML-project
│   README.md
│   MANIFEST.in    
│   mypy.ini
│   pyproject.toml
│   setyp.py
│   .gitignore
│   tox.ini
│
└───notebooks
│   │   1. Data Analysis.ipynb
│   │   2. Feature Engineering.ipynb
│   │   3. Feature Engineering Pipeline.ipynb
│   │   4. Machine Learning.ipynb
│   │   preprocess.py
│   
└───requirements
│   │   requirements.txt
│   │   research-env.txt
│   │   production.txt
│   │   deployment.txt  
│
└───src
│   │   VERSION
│   │   __init__.py
│   │   config.yml
│   │   pipeline.py
│   │   train_pipeline.py
│   │   predict.py
│   │
│   └───config 
│   │   │   __init__.py
│   │   │   core.py
│   │ 
│   └───data 
│   │   │   __init__.py
│   │   │   train.csv
│   │   │   test.csv
│   │     
│   └───processing 
│   │   │   __init__.py
│   │   │   data_manager.py
│   │   │   features.py
│   │  
│   └───trained_models 
│   │   │   __init__.py  
```

### Steps in An End-to-end ML Project

1. Start with jupyter notebooks and finalize a model.
2. Transform research code to production code.
3. Make the project a package.
4. Serve it via a REST API.
5. Dockerize it and deploy it.

### 1. Start with jupyter notebooks and finalize a model

The ```notebooks``` folder is the research which is often done by a Data Scientist.

Usually a Data Analysis notebook for EDA and data understanding is the first step.
Then, feature are created in a pipeline. Here, sciki-learn and feature-engine were used.
Finally, the ML model is placed at the end of the pipeline.

Research can be very time-consuming. Here, a simple pipeline is created, 
because the creation of a 95% accuracy model is out of the scope of this work.

### 2. Transform research code to production code

The ```src``` folder is the transformation of the jupyter notebooks to a python project.

Some good practices:
- Create a ```config.yml``` file that contains all the constants and configurations derived from the notebooks. Accompany it with a .py file to parse it (Here it is the ```src/config/core.py```).
- Tidy all extra functions written and place them in a ```processing``` folder. For example, in ```src/processing/data_manager.py``` there are functions to read the data, save, read, and remove the pipeline.
- Make different file for ```train_pipeline.py``` and ```predict.py```.
- Always create very small functions to test them easier and have a readable code.
- Create a ```trained_models``` folder to deposit the models.
- Have a ```VERSION``` file, to track the version of the project, e.g. 0.0.4
- Write ```tests```. Now write more tests.
- Make a ```tox.ini``` file to make life easier, test code faster, get rid of styling, type checks, linting, and PEP8 concerns. 

Note: In order to import your python files as packages in other python files, we need to add the project's filepath to the Path environmental Variable.

### 3. Make the project a package

We need 3 files in the root of the project:

1. ```MANIFEST.ini```: Define which files to include and exclude from the package.
2. ```pyproject.toml```: Specify basic dependencies and configure tooling.
3. ```setup.py```: Package metadata, version, requirements, how to create the package.

From the project directory: ```python -m build```

Then, make an account to PyPI. Install twine: ```pip install twine```

Upload: ```twine upload dist/end_to_end_ML_project-0.0.4-py3-none-any.whl```

Now the package can be installed like any other package with ```pip install end-to-end-ML-project```

It can be imported like: ```import src```


### 4. Serve it via a REST API

The API should be a different repository or at least a different folder. Here it is located in the folder ```app-fastapi```.

The first thing here is in the ```requirements.txt```, where we define to install the ```end-to-end-ML-project``` package,
which we have published earlier.

Three key files of the api are:

- ```config.py```: Specify metadata of the api, and logging settings.
- ```main.py```: Define the main app and the index page router.
- ```api.py```: Define a health and a predict endpoint.

We define some ```schemas``` for automatic validation of variable types.

We also define ```tests``` with predefined input data to predict.

We also use ```logging``` and the package ```loguru```.


### 5. Dockerize it and deploy it

WIP
