"""
Used to evaluate which version of the models is the best based on a certain test
"""

import os, sys

arch = input("which architecture?\n")
test = input("which test?\n")
# version  = input("which version of the data?\n")
version ="1"
averages={}
if test=="dropout":
    values = [i/10 for i in range(2,8)]
elif test=="dim":
    values = [i for i in range(100, 600, 100)]
elif test=="enc":
    values = [i for i in range(200,1100,200)]
    if arch == "transformer":
        values = values + [1024, 1280, 1536, 1792, 2048]

for value in values:
    command = f"python .\eval_script.py {test} {value} {arch} dev {version} ndebele swati xhosa zulu"
    os.system(command)

for value in values:
    with open(f"results/{test}_{arch}_{value}dev_v{version}.tsv") as f:
        x = f.readlines()
    
    avg = float((x[6].split("\t"))[3])
    averages[avg] = value

# averages.sort()
# best = values[averages.index(max(averages))]

# print(f"The best {test} setting for the {arch} is: {best}.")
keys_in_order = sorted(averages.keys(), reverse=True)
for i in keys_in_order:
    print(f"{averages.get(i)}: {i}")

print("-"*40)
best_value=averages.get(keys_in_order[0])
os.system(f"python .\eval_script.py {test} {best_value} {arch} test {version} ndebele swati xhosa zulu")

with open(f"results/{test}_{arch}_{best_value}test_v{version}.tsv") as f:
    x = f.readlines()

avg = float((x[6].split("\t"))[3])
print("Test Results:")
print(f"{best_value}: {avg}")

clean = input("Clean files (y/n)?\n")
if clean=="y":
    try:
        os.system("del /Q .\\results\\*")
    except:
        print(sys.exc_info()[0])

