import sys
import subprocess
import glob

def remove_extension(filename):
    for i in range(0, len(filename)):
        if filename[i] == '.':
            return filename[0:i]

def main(dir):
    heic_files = glob.glob(dir + "/*.heic") + glob.glob(dir + "/*.HEIC")
    for filename in heic_files:
        print(filename)
        command = ("heif-convert -q 100 " + filename + " " + remove_extension(filename) + ".png")
        subprocess.call(command, shell=True)

if __name__ == '__main__':
    main(sys.argv[1])