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
            # echo "Inited python venv"
            export PATH="${VENV_BIN_DIR}:${PATH}"
        else
            echo "Error on init python venv"
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

_generate_file() {
    python3 "${MAIN_SCRIPT_PATH}"

    if [ $? -eq 0 ]; then
        echo -e "\nCV file generated successfully!\n"
        find "${OUTPUT_DIR}" -type f -name '*.docx'
    else
        echo -e "\nFail on generate CV file\n"
        exit 5;
    fi
}

_init_env
_install_requirements
_generate_file
