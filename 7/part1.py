from functools import reduce
import operator

class Solution:

    def set_in_tree(self, tree, file_path, key, value):
        c_dir = reduce(operator.getitem, file_path, tree)
        c_dir[key] = value

    def get_dir_size(self, file_tree):
        dir_size = 0
        for key in file_tree:        
            if type(file_tree[key]) == dict:
                dir_size += self.get_dir_size(file_tree[key])
            else:
                dir_size += file_tree[key]
        
        if dir_size < 100_000:
            self.total += dir_size

        return dir_size

    def __init__(self) -> None:    
        self.total = 0
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
            dir_size = self.get_dir_size(file_tree)
            print(dir_size, self.total)

Solution()
