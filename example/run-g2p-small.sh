#!/bin/bash
arch=hard
for data in ndebele swati xhosa zulu; do
    python src/train.py \
        --dataset g2p \
        --train data/$data/$data.train \
        --dev data/$data/$data.dev \
        --test data/$data/$data.test \
        --model model/g2p/small/$arch/$data \
        --embed_dim 100 --src_hs 200 --trg_hs 200 --dropout 0.2 \
        --arch $arch --gpuid 0 --estop 1e-8 --epochs 50 --bs 20
done