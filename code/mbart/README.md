# Mulda MBART Model
The code is modified on top of [fairseq](https://github.com/pytorch/fairseq).

## Install 
```
pip install --editable ./
```

## Data Preprocessing
First tokenize the linearized sentences and prepend/append language tags.

```
bin/tokenization.sh

# Examples of generated data.
# src
▁Only ▁B - ORG ▁Se at ▁and <mask> [en_XX]

# tgt
[en_XX] ▁Only ▁B - ORG ▁Se at ▁and ▁B - ORG ▁Porsche ▁had ▁few er ▁registration s ▁in ▁July ▁1996 ▁compared ▁to ▁last ▁year ▁' s ▁July ▁ .
```

Then convert files to binary format. More details can be found in the [fairseq](https://github.com/pytorch/fairseq) project.

```
bash bin/preprocess.sh
```

## Finetune

Run the below commands to finetune mbart model and generate synthetic labeled sentences. Then follow the steps descriped in our paper to filter the data using NER model.
```
bash bin/finetune.sh
bash bin/gen.sh
```

