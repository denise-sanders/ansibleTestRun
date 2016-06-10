import daemon
from flask import Flask
import important_not_a_daemon #the other module

with daemon.DaemonContext():
	important()
