# python3

import sys
import threading


def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for child, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(child)
    
    def get_height(node):
        if not children[node]:
            return 1
        else:
            return 1 + max(get_height(child) for child in children[node])
    
    root = parents.index(-1)
    return get_height(root)
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height
    #max_height = 0

 
                
def main():
    text = input("'I' for input, 'F' for file: ")
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))

    elif "F" in text:
        path = './test/'
        file_name = input("File name: ")
        folder = path + file_name
    
        if 'a' in file_name:
            print("File can not contain letter 'a'")
            return
        try:
            with open(folder, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("File not found")
            return
        except ValueError:
            print("Invalid input format")
            return
    else:
        print("Type 'I' or 'F': ")
        return 

    print(compute_height(n, parents))

    # implement input form keyboard and from file
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#if __name__ == "__main__":
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
