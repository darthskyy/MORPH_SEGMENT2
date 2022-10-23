import sys

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

    
    return f"{lang.title()}\t{round(precision*100,3)}\t{round(recall*100,3)}\t{round(f_score*100,3)}"



def main():
    n = len(sys.argv)

    if n>1:
            test = sys.argv[1]
            attn = sys.argv[3]
            resultset = sys.argv[4]
            rate= float(sys.argv[2])
            with open(f"results/{test}_{attn}_{rate}{resultset}.tsv", "w") as f:
                dropout = f"transformer{rate:f}".rstrip("0")
                print(f"{attn}_{test}_{rate}{resultset}", file=f)
                print("Language","P","R","F1",sep="\t",file=f)
                for i in range(5, n):
                    lang = sys.argv[i]
                    path = f"model/test/{test}/{attn}/test{rate}/{lang}.decode.{resultset}.tsv"
                    pred, trg = process_results(path, lang)
                    results = eval_morph_segments(pred, trg, lang)
                    print(results, file=f)
    else:
        print(f"No files were provided for {sys.argv[0]}")

def main2():
    print("\t*")
    print("12345678*")

if __name__=="__main__":
    main()
