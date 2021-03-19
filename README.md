# IRS-tax-from-search

### Python version used
    - Python 3.6.9


### How to Run the program 

### Prerequisites
    - Python3

### Create and activate a virtual environment in the IRS-tax-form-search directory
```sh
$ virtualenv env
```

### Install requirements
```sh
$ pip3 install -r requirements.txt
```

### Run the main.py with commands
- When you want to get data of a list of forms as json
  example)
```sh
$ python3 main.py search "Form W-2" "Form 1095-C" "Form 706-NA"
```

- When you want to download tax forms 

  example)
```sh
$ python3 main.py download "Form W-2" "2018-2020"
```





