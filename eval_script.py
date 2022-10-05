import sys

def process_results(lang: str):
    pred = []
    target = []


    with open(f"model/g2p/large/transformer/{lang}.decode.test.tsv", "r") as resultFile:
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

    sepr = "\t" if lang!="ndebele" else ""
    print(f"Language: {lang.title()}{sepr}", f"P: {round(precision*100,3)}", f"R: {round(recall*100,3)}", f"F1: {round(f_score*100,3)}", sep="\t")



def main():
    n = len(sys.argv)

    if n>1:
        for i in range(1, n):
            lang = sys.argv[i]
            pred, trg = process_results(lang)
            eval_morph_segments(pred, trg, lang)
    else:
        print(f"No files were provided for {sys.argv[0]}")

def main2():
    print("\t*")
    print("12345678*")

if __name__=="__main__":
    main()
