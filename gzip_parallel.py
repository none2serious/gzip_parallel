#!/usr/bin/env python3

from multiprocessing import Pool
import glob
import os
import argparse
import time
import numpy as np
from datetime import datetime

class gzip_parallel(object):
    def __init__(self,
                 logfile:str,
                 num_cores:int,
                 pattern:str,
                 decompress:bool=False)->None:
        
        self.logfile = logfile
        self.num_cores = num_cores
        self.pattern = pattern
        self.do_decomp = decompress
        
    def write_log_header(self) -> None:
        with open(self.logfile, "w") as f:
            f.write("------------------------\n")
            now = datetime.now()
            f.write(f"{now.strftime('%c')}\n")
            f.write("------------------------\n")
            f.write("Compression Results:\n")
            f.write(f"{'unzipped':11}{'gzipped':11}{'comp%':7} filename\n")
            
    def compress(self, x):
        x_full = self.abspath(x)
        cmd = f"gzip {x_full}"
        orig_size = os.path.getsize(x_full)
        os.system(cmd)
        zip_size = os.path.getsize(f"{x_full}.gz")
        self.log_progress(orig_size, zip_size, x_full)


    def decompress(self, x):
        x_full = self.abspath(x)
        x_uncompressed = self.abspath(x, strip_ext=True)
        zip_size = os.path.getsize(x_full)
        cmd = f"gzip -d {x_full}"
        os.system(cmd)
        orig_size = os.path.getsize(x_uncompressed)
        self.log_progress(orig_size, zip_size, x_full)


    def human_size(self, size):
        """Get file in size in human readable format."""
        if size >= np.power(1024, 4):
            size /= np.power(1024, 4)
            suffix = "TB"
        elif size >= np.power(1024, 3):
            size /= np.power(1024, 3)
            suffix = "GB"
        elif size >= np.power(1024, 2):
            size /= np.power(1024, 2)
            suffix = "MB"
        elif size >= 1024:
            size /= 1024
            suffix = "KB"
        else:
            suffix = "bytes"
        return f"{np.round(size,1)} {suffix}"


    def log_progress(self, orig, zipped, fname):
        raw_size = self.human_size(orig)
        zip_size = self.human_size(zipped)
        change = 1 - (zipped / orig)
        change *= 100
        log_row = f"{raw_size:10} {zip_size:9}  {change:3.2f}%  {fname}\n"
        with open(self.logfile, "a") as f:
            f.write(log_row)
        print(log_row.strip())


    def abspath(self, fname, strip_ext=False):
        fullpath = os.path.abspath(os.path.expanduser(fname))
        head, tail = os.path.split(fullpath)
        if strip_ext is True:
            tail = ".".join(tail.split(".")[:-1])
        return f"{head}/{tail}"


    def time_summary(self, start:float, end:float)-> str:
        summary = f"""
        ----------------------------------
            Total time: {end-start:3.2f} seconds.
        ----------------------------------

        """
        return summary

    def run(self):
        start = time.time()
        self.write_log_header()
        flist = glob.glob(self.pattern)
        if self.do_decomp is True:
            with Pool(self.num_cores) as p:
                p.map(self.decompress, flist)
        else:
            with Pool(self.num_cores) as p:
                p.map(self.compress, flist)
        
        end = time.time()
        summary = self.time_summary(start, end)
        print(summary)
        with open(self.logfile, "a") as f:
            f.write(summary)

                
def main():
        parser = argparse.ArgumentParser(description="Gzip with multiple processes")
        parser.add_argument(
            "--pattern",
            dest="pattern",
            required=True,
            help="Search string for files e.g. '*.csv' or '*.csv.gz'",
        )

        parser.add_argument(
            "--num_cores",
            dest="num_cores",
            default=4,
            type=int,
            help="The number of cores to use; default=4",
        )

        parser.add_argument(
            "--logfile",
            dest="logfile",
            default="./gzip_parallel.log",
            help="The log file to create.",
        )

        parser.add_argument(
            "-d",
            dest="decompress",
            action="store_true",
            help="The flag '-d' will cause the program to decompress files matching the pattern",
        )

        args = parser.parse_args()

        gp = gzip_parallel(logfile=args.logfile,
                           num_cores=args.num_cores,
                           decompress=args.decompress,
                           pattern=args.pattern)
        gp.run()

if __name__ == "__main__":
    print("------------------------")
    print("Compression Progress:")
    print(f"{'unzipped':11}{'gzipped':11}{'comp%':7} filename")

    main()
