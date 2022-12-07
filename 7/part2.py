from functools import reduce
import operator
import math

class Solution:

    def set_in_tree(self, tree, file_path, key, value):
        c_dir = reduce(operator.getitem, file_path, tree)
        c_dir[key] = value

    def get_dir_size(self, file_tree, dir_name):
        dir_size = 0
        for key in file_tree:        
            if type(file_tree[key]) == dict:
                dir_size += self.get_dir_size(file_tree[key], key)
            else:
                dir_size += file_tree[key]
        
        print(dir_name, dir_size)
        self.dir_sizes.append(dir_size)

        return dir_size

    def __init__(self) -> None:    
        self.dir_sizes = []
        self.total_space = 70_000_000
        self.required_space = 30_000_000

        with open ("./data.txt", "r") as file:
            
            data = file.readlines()

            file_tree = {"/" : {}}

            pwd = "/"
            for line in data:
                tokens = line.strip("\n").split(" ")

                if tokens[0] == "$":
                    if tokens[1] == "cd":
                        if tokens[2] == "..":
                            pwd = "/".join(pwd.split("/")[:-2])+"/"
                        elif tokens[2] == "/":
                            pwd = "/"
                        else:
                            pwd += (tokens[2] + "/")
                else:
                    file_path = ["/"] + list(filter(lambda k: k != "", pwd.split("/")))
                    if tokens[0] == "dir":
                        self.set_in_tree(file_tree, file_path, tokens[1], {})
                    else:
                        self.set_in_tree(file_tree, file_path, tokens[1], int(tokens[0]))
            
            # print(file_tree)
            used_space = self.get_dir_size(file_tree, None)
            # print(used_space)
            open_space = self.total_space - used_space

            # print(self.dir_sizes, open_space)
            for dir_size in list(sorted(self.dir_sizes)):
                if dir_size + open_space >= self.required_space:
                    print(dir_size)
                    break

Solution()
