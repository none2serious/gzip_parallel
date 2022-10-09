# gzip_parallel
Simple multithreaded gzip script

usage: gzip_parallel.py [-h] --pattern PATTERN [--num_cores NUM_CORES] [--logdir LOGDIR] [-d]

Gzip with multiple processes

optional arguments:
  -h, --help            show this help message and exit
  --pattern PATTERN     Search string for files e.g. '*.csv' or '*.csv.gz'
  --num_cores NUM_CORES
                        The number of cores to use; default=4
  --logdir LOGDIR       The number of cores to use; default=4
  -d                    The flag '-d' will cause the program to decompress files matching the pattern

`e.g. gzip_parallel.py --pattern */*.xdf --num_cores 6 --logdir sub1_sess1_zip.log`
