import os
from shutil import copy, rmtree


def copy_dir(source: str, destination: str) -> None:
    if not os.path.exists(source):
        raise Exception("Source directory not found")
    if not os.path.exists(destination):
        raise Exception("Destination directory not found")
    if not (os.path.isdir(source) and os.path.isdir(destination)):
        raise Exception("Source or Destination is not a directory.")
    rmtree(destination)
    os.mkdir(destination)
    content = os.listdir(source)
    for object in content:
        object_path = os.path.join(source,object)
        if os.path.isfile(object_path):
            copy(object_path, destination)
            print(f"File {object} has been copied to {destination}")
        elif os.path.isdir(object_path):
            os.mkdir(os.path.join(destination,object))
            copy_dir(object_path,os.path.join(destination,object))
            print(f"Directory {object} has been copied to {os.path.join(destination,object)}")
        else:
            raise Exception("An object to copy in copy_dir was neither a filse nor a directory.")
    