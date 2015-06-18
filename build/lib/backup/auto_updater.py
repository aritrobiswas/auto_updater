import os
import sys
from optparse import OptionParser

# The top argument for walk. The
# Python27/Lib/site-packages folder in my case

topdir = '.' #'./temp/backup_practice' # actual directory on my computer: '/home/aritrobiswas/projects/Markdowns/temp/backup_practice'

# The arg argument for walk, and subsequently ext for step
exten = '.txt'


def step(ext, dirname, names):
    ext = ext.lower()

    for name in names:
        if name.lower().endswith(ext):
            file_path = os.path.join(dirname, name)
            os.system("gsutil -m cp " + file_path + " gs://neimanmarcus/aritro/")

# Start the walk
def backup_files_with_walk():
        inf = open("cloud_location.txt")
        location = inf.read()
        os.path.walk(topdir, step, exten)


def backup_files(backup_dir,bucket):
        os.system("gsutil -m cp -R " + backup_dir + " " + cloud_location)


def parse_options(argv):
        parser = OptionParser()
        parser.add_option("-p", "--backup_dir", dest="backup_dir",
                                  help="backup_dir - the directory to back up", default=None)
        parser.add_option("-b", "--bucket", dest="bucket",
                                  help="bucket - the cloud bucket to back up to", default=None)
        (options, args) = parser.parse_args(argv)
        return options.backup_dir, options.bucket

if __name__ == "__main__":
        backup_dir,bucket = parse_options(sys.argv)
        backup_files(backup_dir,bucket)                                     