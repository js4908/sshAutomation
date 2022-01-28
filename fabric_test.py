
from fabric import Connection
c=Connection(host="IP address of host", user="op", connect_kwargs={"password": "login_password_goes here"})
c.run("su")
c.run("root_password_goes_here")
c.run('ls')
