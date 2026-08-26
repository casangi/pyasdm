#
# script to find all of the directories in the given sdm directory
# path and launch a separate instance of python to run asdm_benchmark
# on that directory using the skip_uniqueness value each time
#
# the python instances are run in sequence, not concurrently
#
import argparse
import os
import sys
import subprocess
from pathlib import Path

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run benchmark_asdm on each directory in sdmdir_path"
    )

    parser.add_argument(
        "sdmdir_path", type=str, help="The path to a directory containing SDMs"
    )

    parser.add_argument(
        "--skip_uniqueness",
        action="store_true",
        help="Skip uniqueness checking (default: False)",
    )

    args = parser.parse_args()

    sdmdir_path = os.path.expanduser(args.sdmdir_path)

    if not os.path.isdir(sdmdir_path):
        print(f"{sdmdir_path} is not a directory, existing")
        sys.exit(1)

    print(
        f"Benchmarking using all directories in {sdmdir_path} and skip_uniqueness is {args.skip_uniqueness}"
    )

    root = Path(sdmdir_path)

    subdirs = [path for path in root.iterdir() if path.is_dir()]

    if not subdirs:
        print(f"No possible SDMs found in {sdmdir_path}")
        sys.exit(1)

    subdirs.sort()

    for sdmDir in subdirs:
        sdmDir_path = str(sdmDir.resolve())

        command = [sys.executable, "-u", "benchmark_asdm.py", sdmDir_path]
        if args.skip_uniqueness:
            command.append("--skip_uniqueness")

        process = subprocess.Popen(command)
        process.wait()
