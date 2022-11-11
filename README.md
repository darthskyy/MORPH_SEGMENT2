# MORPH_SEGMENT2

## Canonical Morphological Segmentation for Nguni Languages using Hard Attention
### by Simbarashe Mawere
### supervised by Jan Buys

This repository contains the code that was used by Simbarashe Mawere for the CSC2005Z research project. The Machine Learning models included are the hard attention neural transducer with 2 configurations and a soft attention transformer.

## The Task
The task undertaken is canonically segmenting Nguni language words into their morphemes which are the smallest units in morphology bearing meaning individually.

The significance of this task lies in the preservation of these languages (and possibly by extensio, other agglutinative languages), the development of NLP tools for the languages and possibly instruction and analysis in the study of Linguistics. The morphemes contain a lot of meaning, hence they can be use in situations were meaning of words is paramount such as translation and web-crawling for search engines.

## Experiments

To use the models, we use the data in its respective directory and the files in the example directory to run the models.

```bash
# download the repo and all its data
git clone https://github.com/darthskyy/MORPH_SEGMENT2.git
cd MORPH_SEGMENT2

#run the any one of the models
# large configuration hard attention neural transducer
bash example/large_HNT.sh

# small configuration hard attention neural transducer
bash example/small_HNT.sh

# modified soft attention transformer
bash example/ST.sh

# after the training is done, you can run eval_script.py and follow the prompts
python eval_script.py

# if all the parameters are trained for as in the final report you can run the pick_best.py file to select the best model based on development set performance
python pick_best.py

```

## Acknowledgements
Shijie Wu for the code base for their open-source [neural transducer](https://github.com/shijie-wu/neural-transducer) used in this project
Aaron Daniels, Tumi Moeng and Sheldon Reay for their open-source [MORPH_SEGMENT](https://github.com/DarkPr0digy/MORPH_SEGMENT) repo and evaluation scripts. Most especially for beginning the task which would have been difficult to implement without inspiration from their research
Jan Buys for supervising and teaching me throughout this entire project.