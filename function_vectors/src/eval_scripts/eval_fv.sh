#!/bin/bash
datasets=('sentiment')
# datasets=('antonym' 'ag_news' 'sentiment')
# datasets=('antonym' 'capitalize' 'country-capital' 'english-french' 'present-past' 'singular-plural')
cd /home/jiii111/iclTaskVector/function_vectors

for d_name in "${datasets[@]}"
do
    echo "Running Script for: ${d_name}"
    CUDA_VISIBLE_DEVICES=2,3 python ./src/evaluate_function_vector.py --dataset_name="${d_name}" --save_path_root="results/gptj" --model_name='EleutherAI/gpt-j-6b'
done