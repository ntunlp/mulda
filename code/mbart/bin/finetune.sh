# For convenience, we save the masked sentences in the files for src language (it_IT in this example) as encoder input.
# Note that the same language tag [en_XX] is used in both src and tgt files during data preprocessing. 

PRETRAIN=/home/linlin.liu/research/2020/clda/data/model/mbart/mbart.cc25
langs=ar_AR,cs_CZ,de_DE,en_XX,es_XX,et_EE,fi_FI,fr_XX,gu_IN,hi_IN,it_IT,ja_XX,kk_KZ,ko_KR,lt_LT,lv_LV,my_MM,ne_NP,nl_XX,ro_RO,ru_RU,si_LK,tr_TR,vi_VN,zh_CN
path_2_data=PATH/TO/data/

CUDA_VISIBLE_DEVICES=4 fairseq-train $path_2_data \
  --encoder-normalize-before --decoder-normalize-before \
  --arch mbart_large --layernorm-embedding \
  --task translation_from_pretrained_bart \
  --source-lang it_IT --target-lang en_XX \
  --criterion label_smoothed_cross_entropy --label-smoothing 0.2 \
  --optimizer adam --adam-eps 1e-06 --adam-betas '(0.9, 0.98)' \
  --lr-scheduler polynomial_decay --lr 5e-05 --min-lr -1 --warmup-updates 1000 --total-num-update 550000 \
  --dropout 0.3 --attention-dropout 0.1 --weight-decay 0.0 \
  --max-tokens 512 --update-freq 2 \
  --save-interval 50 --save-interval-updates 20000 --keep-interval-updates 1 --no-epoch-checkpoints \
  --seed 222 --log-format simple --log-interval 2 \
  --restore-file $PRETRAIN \
  --reset-optimizer --reset-meters --reset-dataloader --reset-lr-scheduler \
  --langs $langs \
  --ddp-backend no_c10d \
  --max-epoch 250
