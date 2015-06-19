Usage:

To create a job on the crontab to backup a specified directory at the appropriate google cloud bucket at the specified times, write the following line:
sudo backuputil -p "<directory to back up>" -b "<gcs bucket>" -t "<timing specification>" -f "j"
Example:
sudo backuputil -p "/home/aritrobiswas/projects/auto_updater" -b "gs://neimanmarcus/aritro" -t "* * * * *" -f "j"

To simply backup a directory for the moment, use this:
sudo backuputil -p "<directory to back up>" -b "<gcs bucket>"  -f "n"
Example:
sudo backuputil -p "/home/aritrobiswas/projects/auto_updater" -b "gs://neimanmarcus/aritro" -f "n"

HELPFUL TIPS
1. Make sure to specify the absolute path of the directory to back up as an argument.
