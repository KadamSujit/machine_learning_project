Application url:
[HousingPredictor](https://ml-regression-app.herokuapp.com/)

## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = <>
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = <>

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```


```
python setup.py install
```
```
Description of setup.py file:
It is similar file like requirements.txt used to install all the required data to run our project successfully.

package --> folder
.py file --> module

__init__.py file is used in housing folder to indicate housing folder as a package.
Any folder that has __init__.py file will be considered as a package.

find packages is a library in setuptools which finds all the folders containing __init__ files in a project folder
and returns list of their names so that we can convert them into packages (for e.g housing)
or else
we can also add "-e ." in requirements. txt file. "-e ." does the same thing of finding packages.
This is used for getting all our project related data into libraries

get_requirements_list() is our customised function which we made to get all the list of all the external packages/libraries that are needed for our project. (i.e all information from requirements.txt)
It is done so that we don't have to every time do pip install -r requirements.txt manually.
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir