# Python CV Generator


## Commands

### Load env

```sh
python3 -m venv ./venv
```

- After init `venv`, put this on path:

```sh
export PATH=$(realpath ./venv/bin/):$PATH
```

### Install requirements

```sh
pip install -r requirements.txt
```

### Generate file

```sh
python3 ./main.py
```

-----

## OR run all in a single script

```sh
./generate-cv.sh
```

-----

## ROADMAP

- [] supports data from JSON file
- [] supports multi language
- [] auto release final file
