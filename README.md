# gzip_parallel
### Simple multithreaded gzip script
Takes a pattern string (e.g. '*.csv') and uses multiprocessing.pool to launch gzip to compress all files matching the pattern string using a user-defined number of CPUs. Creates a log. You can also decompress files in a similar fashion (e.g. '*.csv.gz'), but throwing -d flag to decompress. <br>
Requires numpy

```txt
usage: gzip_parallel.py [-h] --pattern PATTERN [--num_cores NUM_CORES] [--logdir LOGDIR] [-d]

Gzip with multiple processes

optional arguments:
  -h, --help            show this help message and exit
  --pattern PATTERN     Search string for files e.g. '*.csv' or '*.csv.gz'
  --num_cores NUM_CORES
                        The number of cores to use; default=4
  --logdir LOGDIR       Where to save the logfile; default=./logfile.log
  -d                    The flag '-d' will cause the program to decompress files matching the pattern

e.g. gzip_parallel.py --pattern '*/*.xdf' --num_cores 6 --logdir sub1_sess1_zip.log
```
<br>
You get a log like this:<br>

```txt

------------------------
Compression Results:
unzipped   gzipped    comp%   filename
103.1 KB   45.6 KB    55.79%  /Projects/example/data/4d313-45a0f0e45cd33a12defbb21c.csv
103.1 KB   45.6 KB    55.81%  /Projects/example/data/4d313-0bfae15224e13d4fc50bacd3.csv
103.1 KB   45.5 KB    55.82%  /Projects/example/data/4d313-f55032badcbf140ee31ad4c2.csv
1.2 MB     535.0 KB   56.37%  /Projects/example/data/4d313-b15fe2d4100c3ad2e4f5b3ac.csv
1.2 MB     535.2 KB   56.35%  /Projects/example/data/4d313-d1afbde3b00aec552341fc24.csv
103.1 KB   45.5 KB    55.83%  /Projects/example/data/4d313-bf1432ca02ad5ee3154fbd0c.csv
103.1 KB   45.6 KB    55.80%  /Projects/example/data/4d313-c24f150d3cb43bae251a0edf.csv
1.2 MB     534.9 KB   56.38%  /Projects/example/data/4d313-10adb3ef413fac4c5ebd2205.csv
1.2 MB     535.2 KB   56.35%  /Projects/example/data/4d313-1324d5bec0daec3b204f5f1a.csv
103.1 KB   45.6 KB    55.80%  /Projects/example/data/4d313-f40bf3dd13205ea54ecb2c1a.csv
103.1 KB   45.6 KB    55.74%  /Projects/example/data/4d313-c5ca022dfbaf04e453e1db31.csv
103.1 KB   45.6 KB    55.77%  /Projects/example/data/4d313-d511ce33bffa4c02420be5da.csv
1.2 MB     534.9 KB   56.37%  /Projects/example/data/4d313-dc30ebd25e234f04b5f1ac1a.csv
1.2 MB     534.9 KB   56.37%  /Projects/example/data/4d313-d2da1e50fbaccef2403b1534.csv
1.2 MB     535.1 KB   56.36%  /Projects/example/data/4d313-e3cc35220b4a5d101ffd4abe.csv
1.2 MB     534.9 KB   56.37%  /Projects/example/data/4d313-ee5d1c1f0f4a2ac0b4253db3.csv
1.2 MB     534.9 KB   56.37%  /Projects/example/data/4d313-4023a32e1ef5bdac5bcf01d4.csv
13.9 MB    6.1 MB     56.34%  /Projects/example/data/4d313-4d1baf0c42def0a35321bce5.csv
13.9 MB    6.1 MB     56.34%  /Projects/example/data/4d313-5de1f0f03bc3125442aeabdc.csv
103.1 KB   45.6 KB    55.75%  /Projects/example/data/4d313-5202acc331a10b4df4eb5fed.csv
1.2 MB     534.7 KB   56.39%  /Projects/example/data/4d313-abad050fd2b541fc3e2ec134.csv
13.9 MB    6.1 MB     56.34%  /Projects/example/data/4d313-f0c54b2dfe2ea13dab10435c.csv
13.9 MB    6.1 MB     56.34%  /Projects/example/data/4d313-3da410503efc5fb1a4b2ced2.csv
13.9 MB    6.1 MB     56.34%  /Projects/example/data/4d313-c3bad12def0becf4550243a1.csv
103.1 KB   45.6 KB    55.74%  /Projects/example/data/4d313-a2d3b4cafb234f51e01ce0d5.csv

    ----------------------------------
        Total time: 1.23 seconds.
    ----------------------------------
```
