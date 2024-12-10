<h1 align="center">RandomPasswordGenerator</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: ISC" src="https://img.shields.io/badge/License-ISC-yellow.svg" />
  </a>
</p>
## Usage

>  It will prompt you how many characters your password is.  The number can be between 8 and 20 (inclusive)
> 
> There are all 26 letters, lower and uppercase, all 10 digits (0-9) and most special characters available for use. Instead of prompting to ask which are available, just made it default with those.
> 

Before executing the commands, make sure that you create a virtual environment. This can be done by running the following command in the root directory of the project.
```shell
python3 -m venv venv
```
or if you are on windows
```shell
python -m venv venv
```

To activate the virtual environment, run the following command in the root directory of the project.
```shell
source venv/bin/activate
```
or if you are on windows using powershell or git bash
```shell
venv\Scripts\activate
```


1. Spin up the redis database using docker-compose. This will create a redis database with the default port 6379:6379. This can be accessed at localhost:6379 using datagrip or any other database client.
```shell
docker compose up -d
```
2. Install the required packages using pip from the root directory
```shell
pip install -r requirements.txt
```
3. Run the main.py file
```shell
python3 src/main.py
```
or if you are on windows
```shell
python src/main.py
```

You can leave the redis database running if you want, that way you can access the passwords you've generated. The key value pair is the name of the person you entered and the value is the password it generates.

## Author

👤 **Parker Martin**

* Github: [@pmarti9](https://github.com/pmarti9)
