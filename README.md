# SFS
SFS - it is a simple FTP server written in Python using the pyftpdlib library.

## 🧩 Requirements:

For the server to work, install the following dependencies:

By using pip:

> $ pip install pyftpdlib

From repository:

> $ sudo apt-get install python3-pyftpdlib

## :hammer_and_wrench: &nbsp; Server Management:

> [!IMPORTANT]
> Before you begin, change the working server folder in the "server.py" file!

Run:
> $ sudo python3 server.py

Stop:
> $ ps -ef | grep ftpserver | grep -v grep | awk '{print $2}'
