# Makefile for the simple page server.
#

# Nothing to install for this project.
install:
	@(echo 'nothing to install')

restart:
	@(make stop; make clean; make install; make start)

start:
	@(docker build -t image .; docker run -d $$(cat docker_ports.txt) image )

stop:
	@(docker stop $$(docker ps -a -q))

run:
	@(make restart)

clean:
	@(docker rm $$(docker ps -a -q))


