#!/bin/bash
arch=hard

for data in ndebele; do
    python3 src/train.py \
        --dataset g2p \
        --train data/$data/$data.train \
        --dev data/$data/$data.dev \
        --test data/$data/$data.test \
        --model model/example/$arch/$data \
        --embed_dim 300 --src_hs 400 --trg_hs 400 --dropout 0.2 \
        --src_layer 2 --trg_layer 1 --max_norm 5 --nb_sample 4 \
        --arch $arch --gpuid 0 --estop 1e-8 --epochs 50 --bs 20
done
