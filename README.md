[![Python app test with github actions](https://github.com/shruti-mishra8/NLP-WebApp/actions/workflows/devops.yml/badge.svg)](https://github.com/shruti-mishra8/NLP-WebApp/actions/workflows/devops.yml)


# NLP-WebApp

## Creating a virtual environment

1. Create virtual env `virtualenv ~/.venv`
2. Enter into bashrc to enable automatic activation of venv `vim ~/.bashrc`
3. Activation command `source ~/.venv/bin/activate`
4. To apply changes `source ~/.bashrc` or open a new terminal to see changes

## Creating empty files
1. Requirements.txt, Makefile, main.py Dockerfile using touch command [touch requirements.txt]
2. Populate Makefile [To add steps that are invovled in the project life cycle]
3. Populate requirements.txt with all the necessary tools
    3.1 To freeze the version with version number   `pip freeze | less `


## Makind directory
1. mkdir mylib
2. touch mylib/__init__.py [so that python can import it]
3. touch mylib/logic.py [creating a file inside]

## Git push
1. git status
2. git add *
3. git commit -m 'message'
4. git push
