import sys

def rm_char(data):
    st = "" 
    for x in range(len(data)):
        if data[x] == ";":
            return st
        
        st += data[x]
    
    return st


if __name__ == "__main__":

    keys = ["FN:", "TEL;CELL:", ]
    found = []
    try:
        with open(sys.argv[1], "r") as opnr:
            for x in opnr:
                st = x
                for x in range(len(st)):
                    if st[:x] in keys:
                        found.append(rm_char(st[x:]))
    except IndexError:
        print("[-]ERROR Enter The .vcf file Path")

    output = []

    for i in range(len(found)):
        output.append(found[i])
        if len(output) == 2:
            print(output[0])
            print(output[1])
            print("----------------------------------------")
            output = []


