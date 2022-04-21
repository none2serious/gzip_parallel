#!/usr/bin/env python3

from multiprocessing import Pool
import glob
import os
import argparse
import time
import numpy as np


def compress(x):
    x_full = abspath(x)
    cmd = f"gzip {x_full}"
    orig_size = os.path.getsize(x_full)
    os.system(cmd)
    zip_size = os.path.getsize(f"{x_full}.gz")
    log_progress(orig_size, zip_size, x_full)


def decompress(x):
    x_full = abspath(x)
    x_uncompressed = abspath(x, strip_ext=True)
    zip_size = os.path.getsize(x_full)
    cmd = f"gzip -d {x_full}"
    os.system(cmd)
    orig_size = os.path.getsize(x_uncompressed)
    log_progress(orig_size, zip_size, x_full)


def human_size(size):
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


def log_progress(orig, zipped, fname, logdir="./gzip_parallel.log"):
    raw_size = human_size(orig)
    zip_size = human_size(zipped)
    change = 1 - (zipped / orig)
    change *= 100
    log_row = f"{raw_size:10} {zip_size:9}  {change:3.2f}%  {fname}\n"
    with open(logdir, "a") as f:
        f.write(log_row)
    print(log_row.strip())


def abspath(fname, strip_ext=False):
    fullpath = os.path.abspath(os.path.expanduser(fname))
    head, tail = os.path.split(fullpath)
    if strip_ext is True:
        tail = ".".join(tail.split(".")[:-1])
    return f"{head}/{tail}"


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
        help="The number of cores to use; default=4",
    )

    parser.add_argument(
        "--logdir",
        dest="logdir",
        default="./gzip_parallel.log",
        help="The number of cores to use; default=4",
    )

    parser.add_argument(
        "-d",
        dest="decompress",
        action="store_true",
        help="The flag '-d' will cause the program to decompress files matching the pattern",
    )

    args = parser.parse_args()

    flist = glob.glob(args.pattern)
    if args.decompress is True:
        with Pool(args.num_cores) as p:
            p.map(decompress, flist)
    else:
        with Pool(args.num_cores) as p:
            p.map(compress, flist)


def time_summary(start, end):
    summary = f"""
    ----------------------------------
        Total time: {end-start:3.2f} seconds.
    ----------------------------------

    """
    return summary


if __name__ == "__main__":
    start = time.time()
    logdir = "./gzip_parallel.log"
    with open(logdir, "w") as f:
        f.write("------------------------\n")
        f.write("Compression Results:\n")
        f.write(f"{'unzipped':11}{'gzipped':11}{'comp%':7} filename\n")

    print("------------------------")
    print("Compression Progress:")
    print(f"{'unzipped':11}{'gzipped':11}{'comp%':7} filename")

    main()
    end = time.time()
    summary = time_summary(start, end)

    with open(logdir, "a") as f:
        f.write(summary)

    print(summary)
