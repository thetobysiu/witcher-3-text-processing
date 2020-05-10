## Intro
This repo is for text pre-processing Witcher 3 dialog csv into a format suitable for DCTTS/tacotron

## Steps
All scripts all used with an argv, e.g. x.py Geralt
1. (optional) 1_verify_again.py to verify again here, which opens Geralt.csv and an audio folder named Geralt
2. Pre-process the text, filter scenes, append columns of audio length, syllables, counts, language etc. and generates Geralt_processed.csv
3. 3_filter.py is for creating filtered csv suitable for dctts, it is three columns, first column is the audio file index, second column is the original text, third column is the normalized text
4. re-filter Geralt_processed.csv when used after doing audio processing and some audios are deleted.

lj_data.py is for normalizing LJ_Speech metadata.csv