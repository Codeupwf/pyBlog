kill `cat uwsgi.pid`
sleep 1
uwsgi -s 192.168.1.3:5000 --socket-protocol http --module blog --callable app --catch-exceptions --pidfile uwsgi.pid

