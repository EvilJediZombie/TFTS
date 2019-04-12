# TFTS - Transfer Files To Server through a blackhole
import argparse
import os
import shutil


# get input directory
# get output directory
# get permission to delete local copy after transfer
# TODO get how often to check, default continous 
parser = argparse.ArgumentParser(description='Transfer local files to a server.')
parser.add_argument('indir', type=str, help='Input directory to monitor.')
parser.add_argument('outdir', type=str, help='Output directory to transfer files to.')
parser.add_argument('--delete', action='store_true', default=False)
#parser.add_argument('--log', action='store_true', default=True)

args = parser.parse_args()


# Verify that the indir and outdir are valid directories
if not os.path.isdir(args.indir):
    print(args.indir + " is not a valid directory. Exiting.")
    quit()
if not os.path.isdir(args.outdir):
    print(args.outdir + " is not a valid directory. Exiting.")
    quit()

# Copy source files to destination
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        # for any subfolders in the source folder
        if os.path.isdir(s):
            if not os.path.exists(d):
                shutil.copytree(s, d, symlinks, ignore)
        # for any files in the source folder
        else:
            if not os.path.exists(d):
                shutil.copy2(s, d)
        # if user wants to delete the file. this cant be undon
        if args.delete:
            try:
                if os.path.isfile(s):
                    os.remove(s)
                else:
                    shutil.rmtree(s)
            except Exception as e:
                print("Error: ", e)

copytree(args.indir, args.outdir)