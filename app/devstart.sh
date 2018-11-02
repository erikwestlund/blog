#! /usr/bin/env bash
set -e

# If there's a prestart.sh script in the /app directory, run it before starting
PRE_START_PATH=/app/prestart.sh
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    source $PRE_START_PATH
else
    echo "There is no script $PRE_START_PATH"
fi

# Uncomment to test production-like environment
# Start Supervisor, with Nginx and uWSGI
#exec /usr/bin/supervisord

# start app
export FLASK_APP=run
flask run --host=0.0.0.0 --port=80