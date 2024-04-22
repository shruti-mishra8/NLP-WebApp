install:
	# install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#fromat code
	black *.py mylib/*.py
lint:
	#flake8 or pyling
test:
	#test
deploy:
	#deploy
all: install format lint test deploy
 