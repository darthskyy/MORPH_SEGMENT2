"""
This is a subsidiary module which is not part of the MORPH_SEGMENT2 experimentation.
It takes the datasets in the data directory and creates train and dev sets with unique values
and a split 90:10
"""
import random, os

def get_unique(language):

    with open(f"data/{language}/{language}.train", "r", encoding="utf-8") as train:
        x = train.readlines()

    with open(f"data/{language}/{language}.dev", "r", encoding="utf-8") as dev:
        y = dev.readlines()
    
    with open(f"data/{language}/{language}.test", "r", encoding="utf-8") as dev:
        test = dev.readlines()
    

    x1 = set(x)
    y1 = set(y)
    z = x+y
    z1 = list((set(z)))
    print(language)
    print("train: ", len(x), "| unique:", len(x1), sep="\t")
    print("dev: ", len(y), "| unique:", len(y1), sep="\t")
    print("total: ", len(z), "| unique:", len(z1), sep="\t")
    random.shuffle(z1)
    split = int(0.9*len(z1))
    return z1[:split], z1[split:], test

def write_data(language, train, dev, test):
    with open(f"data2/{language}/{language}.train", "w", encoding="utf-8") as f:
            for item in train: print(item, file=f, end="")
        
    with open(f"data2/{language}/{language}.dev", "w", encoding="utf-8") as f:
        for item in dev: print(item, file=f, end="")
    
    with open(f"data2/{language}/{language}.test", "w", encoding="utf-8") as f:
        for item in test: print(item, file=f, end="")

def main():
    if not os.path.exists(".\\data2"):
        os.mkdir(".\\data2")
    
    for language in ["ndebele", "swati", "xhosa", "zulu"]:
        os.system(f"mkdir .\\data2\\{language}")
        train, dev, test = get_unique(language)
        print("-"*15)
        write_data(language, train, dev, test)
        


if __name__=="__main__":
    main()