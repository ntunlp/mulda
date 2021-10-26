model_dir=./checkpoints
langs=ar_AR,cs_CZ,de_DE,en_XX,es_XX,et_EE,fi_FI,fr_XX,gu_IN,hi_IN,it_IT,ja_XX,kk_KZ,ko_KR,lt_LT,lv_LV,my_MM,ne_NP,nl_XX,ro_RO,ru_RU,si_LK,tr_TR,vi_VN,zh_CN
path_2_data=PATH/TO/data/


CUDA_VISIBLE_DEVICES=1 fairseq-generate $path_2_data \
  --path $model_dir/model.pt \
  --task translation_from_pretrained_bart \
  --gen-subset test \
  -s it_IT -t en_XX \
  --bpe 'sentencepiece' --sentencepiece-model $model_dir/sentence.bpe.model \
  --sacrebleu --remove-bpe 'sentencepiece' \
  --batch-size 32 --langs $langs \
  --unkpen 2 --beam 5 > gen

cat gen | grep -P "^H" |sort -V |cut -f 3-  > gen.hyp
