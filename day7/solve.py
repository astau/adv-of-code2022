import re
import pprint

ptcmd = re.compile(r'\$\s(?P<cmd>[a-z]{2})\s*(?P<arg>.*)')
ptdir = re.compile(r'dir\s(?P<dir>.*)')
ptfil = re.compile(r'(?P<size>\d+)\s*(?P<file>[a-z.]*)')

def main():
    data = parse_file("data.txt")
    filesys = traverse_data(data)
    size = calc_size(filesys)

    # Part 1
    dirs = dir_sizes(filesys)
    size = 0
    for d in dirs:
        size += d[0] if d[0] <= 100000 else 0    
    print(f"Answer 1: {size}") # 1517599

    # Part 2
    req_space = 30000000 - (70000000 - filesys['size'])
    print(f"Required Space: {req_space}") # 2476859
    for d in sorted(dirs):
        if d[0] >= req_space:
            print(f"Answer 2: {d[0]}") # 2481982
            break

def dir_sizes(fs):
    result = []
    result.append((fs['size'], fs['path']))
    ch = fs['children']
    if ch != None and len(ch) > 0:
        for c in ch:
            if c['type'] == "D":
                result.extend(dir_sizes(c))
    return result

def calc_size(fs):
    ch = fs['children']
    size = 0;
    if ch != None and len(ch) > 0:
        for c in ch:
            if c['type'] == "F":
                size += c['size']
            else:
                size += calc_size(c)
    fs['size'] = size
    return size

def traverse_data(data):
    filesys = dict()
    pwd = filesys
    for d in data:
        if ptcmd.match(d):
            cmd, arg = ptcmd.match(d).groups()
            if cmd == "cd" and arg == "/":                
                filesys = fs_node(None, "/", "D", [], 0)
                pwd = filesys
            elif cmd == "cd" and arg == "..":
                pwd = pwd["parent"]
            elif cmd == "cd":
                ch = [it for it in pwd["children"] if it["name"] == arg]
                if len(ch) == 0:
                    it = fs_node(pwd, arg, "D", [], 0)
                    pwd["children"].append(it)
                    pwd = it
                else:
                    pwd = ch[0]
            elif cmd == "ls":
                pass
        if ptdir.match(d):
            name = ptdir.match(d).group('dir')
            pwd["children"].append(fs_node(pwd, name, "D", [], 0))
        if ptfil.match(d):
            size, name = ptfil.match(d).groups()
            pwd["children"].append(fs_node(pwd, name, type="F", children=None, size=int(size)))

    return filesys

# { 
#   "path": "/aaa/bbb/ccc",
#   "parent": -reference-,
#   "children": []
#   "type": "F|D"
#   "size": 10101
# }
def fs_node(parent, name, type="F", children=list(), size=0):
    if parent == None:
        path = "/"
    elif parent["path"] == "/":
        path = f"/{name}"
    else:
        path = f"{parent['path']}/{name}"
    return {
        "parent": parent,
        "name": name,
        "path": path,
        "type": type,
        "children": children,
        "size": size
    }


def parse_file(fname):
    with open(fname, "r") as file:
        return file.read().split('\n')

if __name__ == "__main__":
    main()
