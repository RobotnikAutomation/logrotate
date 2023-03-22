# coding=utf-8
import os

dir_logs = 'logs'

contenido = os.listdir(dir_logs)

directorios = []
for i in contenido:
    directorios.append(str(i))

current_folder=os.getcwd()
logrotate = open("logrotate.d/logrotate.conf","w")

logrotate.write("# Include all log files in ~/workspaces/rb_theron/logs/\n")
logrotate.write("# The files will be rotated up to 4 times when they exceed the size 1k or a week has passed.\n") 
logrotate.write("# As the file is rotated every 7 days, 4 times maximum, there will be no files older than 28 days.\n")
logrotate.write("\n")

for i in directorios:
    logrotate.write(current_folder + "/logs/" + i +"/*.log\n")


logrotate.write("{\n")
logrotate.write("maxsize 1k\n")
logrotate.write("weekly\n")
logrotate.write("rotate 4\n")
logrotate.write("nocompress\n")
logrotate.write("notifempty\n")
logrotate.write("create\n")
logrotate.write("}\n")


