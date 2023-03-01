# logrotate

## Crontab file
Crontab is a tool with which you can schedule tasks. 
You can modify the time how often you want a task to be executed by minutes, hours, days, months or years. In this case, the file has been configured to run logrotate every half hour. If we wanted to edit this file, we would only have to do the command:

```bash
crontab -e
```

## Logrotate file
Inside the logrotate.d folder, the logrotate.conf file has been created. The logrotate file can be configured in many ways, with different parameters depending on what you want to do. 
In the following link you can consult the different parameters that can be used to configure the logrotate file.

- [logrotate](https://manpages.ubuntu.com/manpages/impish/es/man8/logrotate.8.html#:~:text=El%20programa%20permite%20la%20rotaci%C3%B3n,se%20ejecuta%20diariamente%20mediante%20cron)

In this case, the objective is to eliminate the log files older than one month, therefore the following parameters have been used.

- maxsize 1k: This parameter indicates the maximum size that the file can have, in this case 1 kilobyte.
- weekly: Rotates the log files every Sunday.
- rotate 4: The log files will be changed 4 times before being removed.
- nocompress: Older versions of the log files are not compressed.
- notifempty: This indicates that the log file is not rotated if it is empty.
- create: Right after the rotation, the new log file with the same name as the newly rotated one is created.


With these parameters the files will be rotated up to 4 times when they exceed the size 1k or a week has passed. Since the file is rotated every 7 days, 4 times maximum, there will be no files older than 28 days.

## Logrotate-state

This file is automatically created when logrotate is executed by cron. It keeps a record of when the last rotations of the different logs have been.

## Logrotate.py
A python code has been created that generates the logrotate.conf file. In this code, you must indicate the logs on which you want to act. For this test, the logs from the rb_theron_relase package have been used.
On the other hand, also in this code you have to indicate the logrotate.conf parameters.

