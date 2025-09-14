import sys
sys.path.append('../')
import my_datasets as md


config = {}
# general
config['exp_name'] = 'exps/task_vector'

# 수정) gpu, model, task
config['gpus'] = ['0','1'] 
config['models'] = ['EleutherAI/gpt-j-6B']  # 'meta-llama/Llama-2-7b-hf', 'gpt2-xl', 
#config['datasets'] = list(md.target_datasets.keys()) # ['agnews', 'dbpedia', 'sst5', 'trec', 'sst2', 'subj', 'mr', 'hate_speech18', 'emo']
config['datasets'] = ['agnews', 'sst2']

config['seed'] = 42
config['run_num'] = 5
config['run_baseline'] = True
config['metric'] = 'acc'  # 'acc', 'macro_f1'
config['bs'] = 2
config['load_in_8bit'] = True # 수정
config['use_cache'] = True

# context vector
config['layer'] = 'all' # all, late, early, mid
config['tok_pos'] = 'last'
config['module'] = ['hidden']  # 'mlp', 'attn', 'hidden'
config['gen_cv_method'] = 'context'  # 'context', 'noise'
config['post_fuse_method'] = 'mean'  # 'mean', 'pca'
config['split_demon'] = False  # split demonstraiton into seperate examples

# data
config['shot_per_class'] = 5
config['val_data_num'] = 32
config['test_data_num'] = 500
config['sample_method'] = 'uniform'  # 'random', 'uniform'
config['use_instruction'] = False
config['add_extra_query'] = True
config['example_separator'] = '\n'