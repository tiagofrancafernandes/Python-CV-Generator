#!/bin/bash

set -e

CURRENT_DIR=$(dirname $(readlink -f "$0"))
VENV_DIR="${CURRENT_DIR}/venv"
VENV_BIN_DIR="${VENV_DIR}/bin"
OUTPUT_DIR="${CURRENT_DIR}/output"
REQUIREMENTS_PATH="${CURRENT_DIR}/requirements.txt"
CURRICULUM_DATA_PATH="${CURRENT_DIR}/curriculum_data.json"
CURRICULUM_DATA_EXAMPLE_PATH="${CURRENT_DIR}/curriculum_data.example.json"
MAIN_SCRIPT_PATH="${CURRENT_DIR}/main.py"

LOAD_ENV_FILE="${CURRENT_DIR}/load-env.sh"

if [ -f $LOAD_ENV_FILE ]; then
    source "${LOAD_ENV_FILE}";
else
    echo -e "\nNot found 'load-env.sh' file\n";
    exit 7;
fi

_generate_file() {
    if [ ! -f $CURRICULUM_DATA_PATH ]; then
        cp "${CURRICULUM_DATA_EXAMPLE_PATH}" "${CURRICULUM_DATA_PATH}"
    fi

    python3 "${MAIN_SCRIPT_PATH}"

    if [ $? -eq 0 ]; then
        echo -e "\nCV file generated successfully!\n"
        echo -e "Files on output dir:\n"
        find "${OUTPUT_DIR}" -maxdepth 1 -type f -name '*.docx'
    else
        echo -e "\nFail on generate CV file\n"
        exit 5;
    fi
}

_init_env
_install_requirements
_generate_file
