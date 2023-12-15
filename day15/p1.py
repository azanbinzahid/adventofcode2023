def read(filename='in.txt'):
    with open(filename, 'r') as f:
        for line in f.readlines():
            return line.split(",")


def hash(string):
    curr = 0
    for s in string:
        curr = curr +  ord(s)
        curr = curr * 17
        curr = curr % 256

    return curr

def solve(str_list):
    ans = 0
    for string in str_list:
        ans+=hash(string)
    
    print(ans)

if __name__ == "__main__":
    str_list = read()
    solve(str_list)
