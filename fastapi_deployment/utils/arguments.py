import argparse
import os

from common.schema.class_mapping import MODEL_CLASSES, TASK_TYPES, DATASET_TYPES

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_args():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--root_path", default=os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                        type=str, required=False, help="The root path of the project.")
    parser.add_argument("--data_dir", default=None, type=str, required=False,
                        help="The input data dir. Should contain the .tsy files (or other data files) for the task.")
    parser.add_argument("--model_type", default=None, type=str, required=False,
                        help="Model type selected in the list: " + ", ".join(MODEL_CLASSES.keys()))
    parser.add_argument("--model_name_or_path", default=None, type=str, required=False,
                        help="Path to pre-trained model or shortcut name selected in the list:")
    parser.add_argument("--dataset_name", default=None, type=str, required=False,
                        help="The name of the dataset to train selected in the list: " + ", ".join(
                            DATASET_TYPES.keys()))
    parser.add_argument("--task_name", default=None, type=str, required=False,
                        help="The name of the task to train selected in the list: " + ", ".join(TASK_TYPES))
    parser.add_argument("--output_dir", default=f"{ROOT_PATH}/checkpoints",  # 获取当前工作目录路径
                        type=str,
                        required=False,
                        help="The output directory where the model predictions and checkpoints will be written.")

    # Other parameters
    parser.add_argument("--config_name", default="", type=str,
                        help="pretrained config name or path if not the same as model_name")
    parser.add_argument("--tokenizer_name", default="", type=str,
                        help="pretrained tokenizer name or path if not the same as model_name")
    parser.add_argument("--cache_dir", default="", type=str,
                        help="Where do you want to store the pre-trained models downloaded from s3")
    parser.add_argument("--max_seq_length", default=128, type=int,
                        help="The maximum total input sequence length after tokenization. Sequences longer "
                             "than this will be truncated, sequences shorter will be padded.")
    parser.add_argument("--do_train", action='store_true', help="Whether to run training.")
    parser.add_argument("--do_eval", action='store_true', help="Whether to run eval on the dev set.")
    parser.add_argument("--do_predict", action='store_true', help="Whether to run predict on the test set.")
    parser.add_argument("--evaluate_during_training", action='store_true',
                        help="Rul evaluation during training at each logging step.")
    parser.add_argument("--do_lower_case", action='store_true', help="Set this flag if you are using an uncased model.")

    parser.add_argument("--per_gpu_train_batch_size", default=8, type=int,
                        help="Batch size per GPU/CPu for training.")
    parser.add_argument("--per_gpu_eval_batch_size", default=8, type=int,
                        help="Batch size per GPu/cPu for evaluation.")
    parser.add_argument('--gradient_accumulation_steps', type=int, default=1,
                        help="Number of updates steps to accumulate before performing a backward/update pass.")
    parser.add_argument("--learning_rate", default=5e-5, type=float,
                        help="The initial learning rate for Adam.")
    parser.add_argument("--weight_decay", default=0.0, type=float,
                        help="Weight decay if we apply some .")
    parser.add_argument("--adam_epsilon", default=1e-8, type=float,
                        help="Epsilon for Adam optimizer.")
    parser.add_argument("--max_grad_norm", default=1., type=float,
                        help="Max gradient norm.")
    parser.add_argument("--num_train_epochs", default=1.0, type=float,
                        help="Total number of training epochs to perform.")
    parser.add_argument("--max_steps", default=-1, type=int,
                        help="If > 0: set total number of training steps to perform. Override num_train_epochs.")
    parser.add_argument("--warmup_steps", default=0, type=int,
                        help="Linear warmup over warmup_steps.")

    parser.add_argument('--logging_steps', type=int, default=500,
                        help="Log every X updates steps.")
    parser.add_argument('--save_steps', type=int, default=500,
                        help="Save checkpoint every X updates steps.")
    parser.add_argument("--eval_all_checkpoints", action='store_true',
                        help="Evaluate all checkpoints starting with the same prefix as model_name ending with step number")
    parser.add_argument("--no_cuda", action='store_true',
                        help="Avoid using CUDA when available ")
    parser.add_argument('--overwrite_output_dir', action='store_true',
                        help="Overwrite the content of the output directory")
    parser.add_argument('--overwrite_cache', action='store_true',
                        help="Overwrite the cached training and evaluation sets")
    parser.add_argument('--seed', type=int, default=42,
                        help="random seed for initialization")

    parser.add_argument('--fp16', action='store_true',
                        help="Whether to use 16-bit (mixed) precision (through NVIDIA apex) instead of 32-bit")
    parser.add_argument('--fp16_opt_level', type=str, default='01',
                        help="For fp16: Apex AMP optimization level selected in ['0g', '01', '02', and '03']."
                             "see details at https://nvidia.github.io/apex/amp.html")
    parser.add_argument("--local_rank", type=int, default=-1,
                        help="For distributed training; local_rank")

    parser.add_argument("--local", type=bool, default=True,
                        help="Decide implement local or cloud deployment.")
    parser.add_argument('--aws_id', type=str, help="Amazon aws S3 bucket id")
    parser.add_argument('--aws_key', type=str, help="Amazon aws S3 bucket key")
    parser.add_argument('--aws_bucket', type=str, default='mydeploybucket2',
                        help="Amazon aws S3 bucket name for deployment")

    args = parser.parse_args()
    return args


args = get_args()
