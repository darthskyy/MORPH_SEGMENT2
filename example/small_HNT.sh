#!/bin/bash
arch=transformer
data=ndebele
python3 src/train.py \
    --dataset g2p \
    --train data/$data/$data.train \
    --dev data/$data/$data.dev \
    --test data/$data/$data.test \
    --model model/example/small_HNT/$data \
    --embed_dim 100 --src_hs 200 --trg_hs 200 --dropout 0.2 \
    --arch $arch --gpuid 0 --estop 1e-8 --epochs 50 --bs 20
