#!/bin/bash
VERSION=1.0
echo "Building Cafeteria app version "$VERSION
# shellcheck disable=SC2006
MY_PATH="`dirname \"$0\"`"              # relative
# shellcheck disable=SC2006
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolute and normalized
if [ -z "$MY_PATH" ] ; then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  exit 1  # fail
fi
# shellcheck disable=SC2164
# shellcheck disable=SC2086
cd $MY_PATH/../
apt-get install python3 python3-pip
echo "--- Running automated tests for Cafeteria app ---"
python test_main.py -v
echo "Setup done Successfully!"