#!/bin/sh

PIDFILE=/var/www/suscriptor/run/suscriptor.pid
#mount /var/www/cloudfood/casapiedra.vd /var/www/cloudfood/casapiedra

case $1 in 
start)
NAME="suscriptor"
DJANGODIR=/var/www/suscriptor/
SOCKFILE=/var/www/suscriptor/run/gunicorn.sock
USER=root
GROUP=root
NUM_WORKERS=2
DJANGO_SETTINGS_MODULE=src.settings
DJANGO_WSGI_MODULE=src.wsgi
echo "Starting $NAME as `whoami`"
cd $DJANGODIR
source /var/www/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
# Start your Django Unicorn# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
/var/www/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=- \
--pid=$PIDFILE &
;;
stop)
kill -9 $(cat $PIDFILE)
rm $PIDFILE
;;
restart)
/etc/init.d/suscriptor.sh stop
/etc/init.d/suscriptor.sh start
;;

esac

exit 0

