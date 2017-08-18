#!/usr/bin/env bash

if [[ $# -ne 2 ]] ; then
    echo "Incorrect parameters number."
    exit 1
fi

PROBLEM_NO=$2
USERNAME=$1

if ! [[ $2 =~ "$2" ]] ; then
    echo "Format error: the first parameter should be a number"
    exit 1
fi

cd "$(dirname "${BASH_SOURCE[0]}")"
if [[ -e "env" ]] ; then
    echo "Enable python virtual environment"
    source ./env/bin/activate
fi

SOLUTION_FOLDERS=$(find ${PROBLEM_NO}-* -depth 0)

if [ $(echo ${SOLUTION_FOLDERS} | wc -l) -ne 1 ]; then
    echo "Cant find the solution with problem number ${PROBLEM_NO}"
fi

TARGET=$(echo ${SOLUTION_FOLDERS} | head -1)

cd ${TARGET}

if [[ -e "./${USERNAME}.py" ]] ; then
    python ./${USERNAME}.py
elif [[ -d "./${USERNAME}" ]] ; then
    cd "./${USERNAME}"
    if [[ -e "./main.py" ]] ; then
        python ./main.py
    elif [[ -e "./run/py" ]] ; then
        python ./run.py
    elif [[ -e "./${USERNAME}.py" ]] ; then
        python ./${USERNAME}.py
    fi
else
    echo "Can't find runnable file."
    exit 1
fi
