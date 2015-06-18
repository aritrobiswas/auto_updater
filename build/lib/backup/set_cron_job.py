import os
import sys
import inspect

def set_cron_job(backup_time,backup_dir,cloud_loc):
        """
        Sets a cron job at the specified backup_time to back up the
        files in the specified directory at the specified cloud location
        """
        os.system("sudo touch cron_container.txt")
        os.system("crontab -l > cron_container.txt")
        crontab_cmd = backup_time + " sudo backuputil -p " + backup_dir + " -b " + cloud_loc
        os.system('echo "' + crontab_cmd + '" >> cron_container.txt')
        os.system("crontab cron_container.txt")
        os.system("rm cron_container.txt")


if __name__ == "__main__":
        #print os.getcwd()
        backup_dir = input("Enter directory to be backed up: ")
        backup_time = input("Enter backup time with the time fields in the appropriate locations in cron format'Minute Hour (Day of Month) Month (Day of Week)' with exactly 1 space between each of the time fields:  ")
        cloud_loc = input("Enter cloud location to back up to: ")
        set_cron_job(backup_time,backup_dir, cloud_loc)