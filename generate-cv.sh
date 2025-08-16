#!/bin/bash

set -e

CURRENT_DIR=$(dirname $(readlink -f "$0"))
VENV_DIR="${CURRENT_DIR}/venv"
VENV_BIN_DIR="${VENV_DIR}/bin"
OUTPUT_DIR="${CURRENT_DIR}/output"
REQUIREMENTS_PATH="${CURRENT_DIR}/requirements.txt"
MAIN_SCRIPT_PATH="${CURRENT_DIR}/main.py"

LOAD_ENV_FILE="${CURRENT_DIR}/load-env.sh"

if [ -f $LOAD_ENV_FILE ]; then
    source "${LOAD_ENV_FILE}";
else
    echo -e "\nNot found 'load-env.sh' file\n";
    exit 7;
fi

_init_env
_install_requirements
_generate_file
