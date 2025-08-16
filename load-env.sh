#!/bin/bash

set -e

CURRENT_DIR=$(dirname $(readlink -f "$0"))
VENV_DIR="${CURRENT_DIR}/venv"
VENV_BIN_DIR="${VENV_DIR}/bin"
OUTPUT_DIR="${CURRENT_DIR}/output"
REQUIREMENTS_PATH="${CURRENT_DIR}/requirements.txt"
MAIN_SCRIPT_PATH="${CURRENT_DIR}/main.py"

# export PATH="${VENV_BIN_DIR}:${PATH}"

_command_exists() {
    command -v "$1" > /dev/null 2>&1
}

_init_env() {
    if _command_exists python3; then
        python3 -m venv ${VENV_DIR}
        if [ $? -eq 0 ]; then
            echo "Inited python venv"
            # export PATH="${VENV_BIN_DIR}:${PATH}"
            source "${VENV_BIN_DIR}/activate"
        else
            echo "Error on init python venv"
            exit 5
        fi
    else
        echo "Please install python3"
        exit 1
    fi
}

_install_requirements() {
    if _command_exists pip; then
        pip install -r "${REQUIREMENTS_PATH}" > /dev/null 2>&1
    else
        echo "Please install python3 and pip3"
        exit 1
    fi
}

_init_env
_install_requirements

export PATH

WHICH_COUNT_LINES=$(which python3 | grep "${VENV_BIN_DIR}" | wc -l)

if [ $WHICH_COUNT_LINES -ge 1 ]; then
    echo -e "\n Venv loaded!"
fi
