#!/bin/bash
datasets=('agnews')
# datasets=('antonym' 'ag_news' 'sentiment')
# datasets=('antonym' 'capitalize' 'country-capital' 'english-french' 'present-past' 'singular-plural')
cd //home/jiii111/ICLTV_exp1/I2CL

for d_name in "${datasets[@]}"
do
    echo "Running Script for: ${d_name}"
    CUDA_VISIBLE_DEVICES=3 python ./fv_src/evaluate_function_vector.py \
    --dataset_name="${d_name}" --save_path_root="results/gptj" --model_name='EleutherAI/gpt-j-6b' \
    --test_data_num=500 --val_data_num=32 --sample_method='uniform' --shot_per_class=5 \
    --n_mean_activations_trials=50 --save_path_root="./exps/fv" # ✅ 수정
    2>&1 | tee -a "./exps/fv/${d_name}/run_$(date +%F_%H%M%S)."
done