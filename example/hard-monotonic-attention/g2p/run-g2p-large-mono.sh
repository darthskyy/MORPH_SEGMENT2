#!/bin/bash
arch=transformer
seed=${2:-0}
for data in ndebele swati xhosa zulu; do
    python src/train.py \
        --dataset g2p \
        --train data/$data/$data.train \
        --dev data/$data/$data.dev \
        --test data/$data/$data.test \
        --model model/g2p/large/monotag-$arch/$data \
        --init init/g2p/large/seed-$seed/$data --seed $seed \
        --embed_dim 200 --src_hs 400 --trg_hs 400 --dropout 0.4 \
        --src_layer 2 --trg_layer 1 --max_norm 5 --nb_sample 4 \
        --arch $arch --gpuid 0 --estop 1e-8 --epochs 50 --bs 20 --mono --indtag
done
