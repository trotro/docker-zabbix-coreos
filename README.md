# Docker Zabbix for CoreOS server

This Docker container provides a patched Zabbix agent to monitor a real CoreOS server and all his containers.

The Zabbix agent has been patched to read system informations from these directories:

* */coreos/proc* mapped from */proc* on the real host
* */coreos/dev* mapped from */dev* on the real host
* */coreos/sys* mapped from */sys* on the real host

You can access the Docker REST API through the socket file */coreos/var/run/docker.sock*

## Usage

### Build the image

    # docker build -t bhuisgen/zabbix-agent .

### Run the container

    # docker run -d -p 10050:10050 \
        -v /proc:/coreos/proc -v /sys:/coreos/sys -v /dev:/coreos/dev \
        -v /var/run/docker.sock:/coreos/var/run/docker.sock
        --name zabbix-agent bhuisgen/zabbix-agent <HOSTNAME> <SERVER_IP>

The needed arguments are:
* *HOSTNAME*: name of the host declared in the Zabbix frontend
* *SERVER*: IP address of the Zabbix server
