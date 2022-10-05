# %%

pred = []
target = []

# %%

with open("model\\g2p\\large\\transformer\\swati.decode.test.tsv", "r") as resultFile:
    results = resultFile.readlines()

results = results[1:]
for line in results:
    word = line.split('\t')
    word[0] = word[0].replace(" ","")
    word[1] = word[1].replace(" ","")
    pred.append(word[0].split('-'))
    target.append(word[1].split('-'))

# %%
print(pred[2000])
print(target[2000])

# %%
def eval_morph_segments(predicted, target):
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
    print("P: ", round(precision*100,3),"R: ", round(recall*100,3),"F1: ", round(f_score*100,3))


model_output = [["nga", "ii", "zin", "konzo"], ["wo", "ku", "thol", "akal", "a"], ['na,','ga','phanda' ]]
reference = [["nga", "i", "zin", "khonzo"], ["woku", "thol", "akal", "a"], ['ga','phanda' ]]




# %%
eval_morph_segments(pred, target)

# %%


# %%



