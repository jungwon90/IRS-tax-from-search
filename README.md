# IRS-tax-from-search

### How to Run the program 

### Prerequisites
    - Python3

### Create and activate a virtual environment in the IRS-tax-form-search directory
```sh
$ virtualenv
```

### Install requirements
```sh
$ pip3 install -r requirements.txt
```

### Run the main.py with a list of form names 
- When you want to get data of a list of forms as json
```sh
$ python3 main.py search "Form W-2" "Form 1095-C" "Form 706-GS"
```

- When you want to download tax forms 
```sh
$ python3 main.py download "Form W-2" "2018-2020"
```





