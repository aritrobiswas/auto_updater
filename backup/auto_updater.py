import os
import sys
from optparse import OptionParser

def backup_files(backup_dir,bucket):
    """ Backs up all files in the specified directory to the specified bucket
    """
    os.system("gsutil -m cp -R " + backup_dir + " " + bucket)


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