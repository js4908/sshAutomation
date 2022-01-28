import  subprocess
ffname_exe="plink.exe"
user=""
server=""
password=""
cmd="" #super user name

plink= '{} -ssh -batch {}@{} -pw {} {}'.format(ffname_exe, user, server, password, cmd)
proc = subprocess.Popen(plink, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# print(proc.stdout.readlines())

proc.stdin.write("super_password\n")
proc.stdin.write("ls\n")
print(proc.stdout.readlines())
proc.stdin.flush()
