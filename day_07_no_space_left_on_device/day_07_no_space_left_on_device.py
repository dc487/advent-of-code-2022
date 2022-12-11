import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

class File:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = 0

    def total_size(self):
        return self.size + sum([x.total_size() for x in self.children.values()])

    def is_directory(self):
        return len(self.children) > 0

    def to_string(self):
        return self.name + " (" + ("dir" if self.is_directory() else "file, " + str(self.size)) + ")"
    

if __name__ == "__main__":
    input = load_input()

    root_folder = File("/")
    root_folder.parent = root_folder

    all_files = [root_folder]

    current_folder = root_folder
    for command in input:
        if command.startswith("$ cd"):
            folder_to_open = command[5:]
            if folder_to_open == "/":
                current_folder = root_folder
            elif folder_to_open == "..":
                current_folder = current_folder.parent
            elif folder_to_open in current_folder.children:
                current_folder = current_folder.children[folder_to_open]
            else:
                new_folder = File(folder_to_open, current_folder)
                all_files.append(new_folder)
                current_folder.children[folder_to_open] = new_folder
                current_folder = new_folder
        elif command.startswith("$ ls"):
            continue
        elif command.startswith("$ "):
            print("Error, Unknown command!", command)
        else:
            parts = command.split(" ")
            file_name = parts[1]

            if file_name not in current_folder.children:
                new_file = File(file_name, current_folder)
                all_files.append(new_file)
                current_folder.children[file_name] = new_file

            if parts[0] != "dir":
                current_folder.children[file_name].size = int(parts[0])

    print(sum([x.total_size() for x in all_files if x.is_directory() and x.total_size() <= 100000]))

    remaining_space = 70000000 - root_folder.total_size()
    min_space_required_to_free = 30000000 -  remaining_space

    size_of_folders_that_could_be_deleted = [x.total_size() for x in all_files if x.is_directory() and x.total_size() >= min_space_required_to_free]
    print(min(size_of_folders_that_could_be_deleted))
