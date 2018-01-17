Mateapp
========

[![Build Status](https://travis-ci.org/arsho/dictmate.svg?branch=master)](https://travis-ci.org/arsho/dictmate)
[![Size](https://img.shields.io/github/size/arsho/dictmate/app.py.svg?)](https://github.com/arsho/dictmate/)
[![Codecov](https://codecov.io/github/arsho/dictmate/coverage.svg?branch=master)](https://codecov.io/github/arsho/dictmate)


. See live [https://mateapp.herokuapp.com/](https://mateapp.herokuapp.com/)

## Software Requirements

The following environment is used to develop the application:

- **OS** : Ubuntu 16.04 (64 bit)
- **IDE** : PyCharm Professional (Version: 2017.2.3)
- **Python** : 3.5 (64 bit)

### Necessary Package Installation

- Install virtual environment

		$ python -m virtualenv venv

- Activate virtual environment (Change it based on your OS)

		$ venv\Scripts\activate.bat

- Install necessary packages included in `requirements.txt`

		$ pip install -r requirements.txt
		
		
### To Run the Application

- Activate virtual environment (if not activated)

		$ venv\Scripts\activate.bat

- Run the `application.py`

		$ python app.py

		
### Unit testing

- Activate virtual environment (if not activated)

		$ venv\Scripts\activate.bat

- Run the `tests.py`

		$ python tests.py

![Unittests](Screenshot/unittests.png)		
		
