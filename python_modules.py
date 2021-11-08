import argparse
from zipfile import ZipFile
import os

def create_zipfile(dirpath):
    with ZipFile('samplezipfile.zip', 'w') as zipobj:
        list_of_files = os.listdir(dirpath)
        print(list_of_files)
        for filename in list_of_files:
            zipobj.write(os.path.join(dirpath,filename))
    if os.path.exists('samplezipfile.zip'):
        print("Zip file created succesfully")

def main():
    parser = argparse.ArgumentParser(description='test example')
    parser.add_argument('--dir', '-dirpath', dest='dirpath', required=True, help='Enter the directory path to create zip file')

    args = parser.parse_args()
    create_zipfile(args.dirpath)

if __name__ == "__main__":
    main()
