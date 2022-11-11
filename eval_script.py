import sys, math, os

##evaluation code adapted (and modified) from Moeng et al. MORPH_SEGMENT
##not to be run on it's own
def process_results(path: str, lang: str):
    pred = []
    target = []

    with open(path, "r") as resultFile:
        results = resultFile.readlines()

    results = results[1:]
    for line in results:
        word = line.split('\t')
        word[0] = word[0].replace(" ","")
        word[1] = word[1].replace(" ","")
        pred.append(word[0].split('-'))
        target.append(word[1].split('-'))

    return pred, target


def eval_morph_segments(predicted, target, lang):
    correct = 0.0
    assert len(predicted)==len(target)
    for pred, targ in zip(predicted, target):
        for p in pred:
            if p in targ:
                correct += 1

    predicted_length = sum([len(pred) for pred in predicted])
    target_length = sum([len(targ) for targ in target])

    precision, recall = correct/predicted_length, correct/target_length
    f_score = 2/(1/precision + 1/recall)

    
    return str(f"{lang.title()}\t{round(precision*100,3)}\t{round(recall*100,3)}\t{round(f_score*100,3)}"), precision, recall, f_score

def main():
    n = len(sys.argv)
    languages=[]
    if n>1:
            test = sys.argv[1]
            attn = sys.argv[3]
            resultset = sys.argv[4]
            version = sys.argv[5]
            rate= (sys.argv[2])
            for i in range(6, n):
                languages.append(sys.argv[i])
    else:
        # goes into prompt mode.
        attn = input("Which model are you evaluating?\n")
        test = input("Which hyperparameter are you testing?\n")
        rate = input(f"What is the value of {test} did you use?\n")
        langs = input("What languages would you like to evaluate performance for\nSeparate them with spaces (if you want all of them type \"all\"):\n")
        if langs=="all":
            languages=["ndebele", "swati", "xhosa", "zulu"]
        else:
            langs = langs.split(" ")
            languages = [i.strip().lower() for i in langs]
            
        resultset = "dev"
        version = "1"

    if not os.path.exists(".\\results"):
        os.system("mkdir .\\results")

    with open(f"results/{test}_{attn}_{rate}{resultset}_v{version}.tsv", "w") as f:
        if version=="1": version=""

        print(f"{attn}_{test}_{rate}{resultset}", file=f)
        print("Language","P","R","F1",sep="\t",file=f)

        result_arr = [[],[],[]]
        for lang in languages:
            path = f"model/test{version}/{test}/{attn}/test{rate}/{lang}.decode.{resultset}.tsv"
            try:
                pred, trg = process_results(path, lang)
                results, p, r, f1 = eval_morph_segments(pred, trg, lang)
                result_arr[0].append(p)
                result_arr[1].append(r)
                result_arr[2].append(f1)
                # print(results)
                print(results, file=f)
            except:
                print(lang.capitalize(), "Error", "Error", "Error", sep="\t", file=f)
                continue
        
        for i in range(len(result_arr)): result_arr[i] = sum(result_arr[i])/len(result_arr[i])

        print("Average", round(result_arr[0]*100, 3), round(result_arr[1]*100, 3), round(result_arr[2]*100, 3), sep="\t", file=f)
    

if __name__=="__main__":
    main()
