import os


def find_files(suffix, path):
    paths = list()
    directories = os.listdir(path)

    for directory in directories:
        sub_directory = os.path.join(path, directory)
        if os.path.isdir(sub_directory):
            # recursive call
            new_folder = find_files(suffix, sub_directory)
            paths.extend(new_folder)

        elif suffix == sub_directory[-2:]:
            # if the required suffix is present append it to the paths list
            paths.append(sub_directory)

    return paths


def print_path(directory_list):
    for directory in directory_list:
        print(directory)


test_c = find_files('.c', './testdir')
print_path(test_c)

print("====================================================")

test_h = find_files('.h', './testdir')
print_path(test_h)
