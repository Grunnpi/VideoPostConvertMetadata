import logging
import sys
import argparse
import subprocess


parser=argparse.ArgumentParser()

# Ecole Directe cred
parser.add_argument('--src', help='source', type=str)
parser.add_argument('--dst', help='destination', type=str)
parser.add_argument('--loglevel', help='log level', type=str, default="info")

args=parser.parse_args()

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILENAME = 'C:\\Documents\\[Mes Images]\\[A trier]\\Handbrake_video_convertie\\keep_metadata.log'
level_name = str(args.loglevel)
level = LEVELS.get(level_name, logging.NOTSET)
logging.basicConfig(filename=LOG_FILENAME,level=level,format=FORMAT)

logging.info('Number of arguments: %s',len(sys.argv))
logging.info('Argument List: %s',str(sys.argv))
logging.info("source = %s",str(args.src))
logging.info("destination = %s",str(args.dst))


ffmgeg_exe = "C:\\Dev\\Tools\\ffmpeg\\bin\\ffmpeg.exe"
metadata_file = "C:\\metadata.txt"

extract_metadata = subprocess.run([ffmgeg_exe, '--i "{0}"'.format(str(args.src)), "-c copy -map_metadata 0 -map_metadata:s:v 0:s:v -map_metadata:s:a 0:s:a -f ffmetadata", metadata_file])
logging.info("extract return [%s]",extract_metadata)

import_metadata = subprocess.run([ffmgeg_exe, '--i "{0}"'.format(str(args.dst)), '-i {0}'.format(metadata_file), "-map_metadata 1 -codec copy", str(args.dst) + ".v2"])
logging.info("import return [%s]",import_metadata)
