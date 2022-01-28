import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='IP', username='op', password='login xxxx')
stdin, stdout, stderr = ssh_client.exec_command("su")
time.sleep(0.1) # some enviroment maybe need this.
stdin.write('root_password_goes_here\n')
stdin.write('ls\n')
stdin.flush()
print(stdout.readlines())
ssh_client.close()


