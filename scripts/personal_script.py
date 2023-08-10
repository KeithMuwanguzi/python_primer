import os
import sys
import shutil

file_pattern = '.docx'

def create_destination(path):
    if not os.path.exists(path):
        os.mkdir(path)

def copy_contents(source,dest):
    shutil.move(source,dest)

def find_file_paths(source):
    file_paths = []
    for root,dirs,files in os.walk(source):
        for f in files:
            if file_pattern in f.lower():
                path = os.path.join(source,f)
                file_paths.append(path)
        break
        
    return file_paths

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd,source)
    target_path = os.path.join(cwd,target)
    paths = find_file_paths(source_path)
    create_destination(target_path)
    for path in paths:
        copy_contents(path,target_path)


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 3:
        raise Exception('Please provide a source and target path only.')
    
    source, target = args[1:]

    main(source,target)