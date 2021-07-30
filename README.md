# MulDA
This [repository](https://github.com/ntunlp/mulda.git) contains the source code and data used in our paper "MulDA: A Multilingual Data Augmentation Framework for Low-Resource Cross-Lingual NER" accepted by ACL-IJCNLP 2021.


## Data
The data generated using our labeled sequence translation method can be found in the "data" directory.

## Labled Sequence Translation
```
cd code/translate; python translate.py
```

## lstm-lm: multiilngual LSTM language model
- train lstm-lm on linearized sequences
```
cd code/lstm-lm;

python train.py \
  --train_file PATH/TO/train.linearized.txt \
  --valid_file PATH/TO/dev.linearized.txt \
  --model_file PATH/TO/model.pt \
  --emb_dim 300 \
  --rnn_size 512 \
  --gpuid 0 
```

- generate linearized sequences
```
cd code/lstm-lm;

python generate.py \
  --model_file PATH/TO/model.pt \
  --out_file PATH/TO/out.txt \
  --num_sentences 10000 \
  --temperature 1.0 \
  --seed 3435 \
  --max_sent_length 32 \
  --gpuid 0
```

## tools: tools for data processing
- tools/preprocess.py: sequence linearization
- tools/line2cols.py: convert linearized sequence back to two-column format

# Requirements
- code/lstm-lm/requirements.txt

# Citation
Please cite our paper if you found the resources in this repository useful.
```
@inproceedings{liu-etal-2021-mulda,
    title = "MulDA: A Multilingual Data Augmentation Framework for Low-Resource Cross-Lingual NER",
    author = "Liu Linlin  and
      Ding, Bosheng  and
      Bing, Lidong  and
      Joty, Shafiq  and
      Si, Luo  and
      Miao, Chunyan",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL'21)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
}
```

