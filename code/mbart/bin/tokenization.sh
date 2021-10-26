# tokenization
SPM=PATH/TO/git/sentencepiece/build/src/spm_encode
MODEL=PATH/TO/mbart.cc25/sentence.bpe.model
LINEAR_FILE=PATH/TO/spm/dev-${LANGUAGE}.lin.txt
TK_FILE=PATH/TO/spm/${LANGUAGE}.spm.dev
${SPM} --model=${MODEL} < $LINEAR_FILE > $TK_FILE
