import os


def find_files(suffix, path):
    paths = list()
    if os.listdir(path):
        directories = os.listdir(path)

    for directory in directories:
        sub_directory = os.path.join(path, directory)
        if os.path.isdir(sub_directory):
            # recursive call
            new_folder = find_files(suffix, sub_directory)
            paths.extend(new_folder)

        elif suffix.split('.')[1].lower() == sub_directory.split('.')[-1].lower():
            # if the required suffix is present append it to the paths list
            paths.append(sub_directory)

    return paths


def print_path(directory_list):
    if len(directory_list) == 0:
        print("No Files Found!!!!!")
    else:
        for directory in directory_list:
            print(directory)


test_c = find_files('.c', './testdir')
print_path(test_c)

print("====================================================")

test_h = find_files('.h', './testdir')
print_path(test_h)

print("====================================================")

test_random = find_files('.py', './testdir')
print_path(test_random)
