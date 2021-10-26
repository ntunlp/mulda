SRC=it_IT
TGT=en_XX
TRAIN=train
VALID=dev
TEST=test
NAME=data
DICT=PATH/TO/mbart.cc25/dict.txt
fairseq-preprocess \
  --source-lang ${SRC} \
  --target-lang ${TGT} \
  --trainpref ${DATA_DIR}/${TRAIN}.spm \
  --validpref ${DATA_DIR}/${VALID}.spm \
  --testpref ${DATA_DIR}/${TEST}.spm \
  --destdir ${DATA_DIR}/${NAME} \
  --thresholdtgt 0 \
  --thresholdsrc 0 \
  --srcdict ${DICT} \
  --tgtdict ${DICT} \
  --workers 70
