def remove_anno(segment: str) -> str:
    """
    This method removes the unnecessary annotations from a line of data
    """
    out_string = ""
    out_length=0
    in_bracket = False
    for char in segment:
        if char in "([":
            in_bracket = True
        
        if in_bracket and char not in ")]":
            continue
        else:
            if char in "])" and segment.find(char):
                if out_length!=0 and out_string[out_length-1] != "-":
                    out_string+="-"
                    out_length+=1
                in_bracket=False
            else:
                out_string+=char
                out_length+=1
    
    return out_string[:-2]
            

def process_file(filename: str) -> None:
    """
    Takes one of the .conll files and processes into suitable input files for the neural-transducer g2p dataloader
    """
    # out_filename = filename[:filename.rfind(".")] + "_proc" + filename[filename.rfind("."):]
    out_filename = filename[:filename.find(".")] + filename[filename.find("clean")+5:filename.rfind(".")]
    with open(filename, "r") as f:
        data = f.readlines()[:-1]
    
    for i in range(len(data)):
        items = data[i].split(" | ")
        items = [items[0], items[3]]
        items[1] = remove_anno(items[1])
        items[0], items[1] = " ".join(list(items[0])), " ".join(list(items[1]))
        data[i] = "\t".join(items)
    
    with open(out_filename, "w") as f:
        for item in data:
            print(item,file=f)


def main():
    process_file("data\\ndebele\\ndebele.clean.train.conll")


if __name__=="__main__":
    main()