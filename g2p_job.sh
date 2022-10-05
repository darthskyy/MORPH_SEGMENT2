#!/bin/bash

#PBS -N runG2P
#PBS -l select=1:ncpus=15:ngpus=1
#PBS -l walltime=2:00:00
#PBS -P CSCI1335
#PBS -m abe
#PBS -M 20simbarashem@gmail.com
#PBS -q gpu_1
ulimit -s unlimited

module load chpc/python/anaconda/3-2021.05
source /apps/chpc/bio/anaconda3-2021.05/etc/profile.d/conda.sh
conda activate /home/smawere/.conda/envs/MORPH_SEGMENT2
pwd
cd ${HOME}/lustre/

dataset=$1
arch=transformer

lr=0.001
scheduler=warmupinvsqr
max_steps=20000
warmup=4000
beta2=0.98       # 0.999
label_smooth=0.1 # 0.0
total_eval=50
bs=400 # 256

# transformer
layers=4
hs=1024
embed_dim=256
nb_heads=4
dropout=${2:-0.3}

ckpt_dir=checkpoints/transformer

for data in ndebele swati xhosa zulu; do
    python3 src/train.py \
        --dataset g2p \
        --train data/$data/$data.train \
        --dev data/$data/$data.dev \
        --test data/$data/$data.test \
        --model $ckpt_dir/$arch/g2p-dropout$dropout/$data \
        --embed_dim $embed_dim --src_hs $hs --trg_hs $hs --dropout $dropout --nb_heads $nb_heads \
        --label_smooth $label_smooth --total_eval $total_eval \
        --src_layer $layers --trg_layer $layers --max_norm 1 --lr $lr --shuffle \
        --arch $arch --gpuid 0 --estop 1e-8 --bs $bs --max_steps $max_steps \
        --scheduler $scheduler --warmup_steps $warmup --cleanup_anyway --beta2 $beta2 --bestacc
done