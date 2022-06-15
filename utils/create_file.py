import argparse
import os.path


class FileAlreadyExistsError(Exception):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create file with normalized snake_case style')
    parser.add_argument('file_name', help='Name of python file', nargs='+')
    parser.add_argument('-f', '--folder', help='Name of folder')
    args = parser.parse_args()
    file_name_args = args.file_name
    folder_name = args.folder or ''
    file_name = ''
    
    # file name normalizing
    for i, item in enumerate(file_name_args):
        file_name_args[i] = ''.join(item.split('.'))
        file_name = '_'.join(file_name_args).lower()
        file_name += '.py'
    
    # create filepath
    file_path = os.path.join('..', folder_name, file_name)
    try:
        os.mkdir(os.path.join('..', folder_name))
    except OSError as e:
        pass
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
    else:
        raise FileAlreadyExistsError('This file already exists')
