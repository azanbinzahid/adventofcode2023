from p1 import read, hash

def solve(str_list):
    boxes = {}
    for i in range(256):
        boxes[i] = []


    for string in str_list:

        string = string.replace('-', '=')
        label, value = string.split("=")
        symbol = '=' if value != '' else '-'


        label_hash = hash(label)

        found = False
        for i in range(len(boxes[label_hash])):
            if boxes[label_hash][i][0] == label:
                found = True
                if symbol == '=':
                    boxes[label_hash][i] = (label, value)
                else:
                    boxes[label_hash].remove((label, boxes[label_hash][i][1]))
                    break
        
        if not found and symbol == '=':
            boxes[label_hash].append((label, value))

    ans = 0
    for i in range(256):
        box = boxes[i]
        for j in range(len(box)):
            ans += (i+1) * (j+1) * int(box[j][1])
    
    print(ans)

if __name__ == "__main__":
    str_list = read()
    solve(str_list)
