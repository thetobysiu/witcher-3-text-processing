# SM4701 SIU KING WAI 54412743
import os
import re
import csv
import sys
import librosa
import pandas as pd
from pandarallel import pandarallel
from nlp import tag_and_process
pandarallel.initialize()


def get_parameter():
    try:
        return sys.argv[1]
    except IndexError:
        print('Please specify file name')
        sys.exit(1)


class WitcherData:
    wav_folder = ''  # The directory that contains the character wav files

    def __init__(self, filename):
        self.filename = os.path.splitext(filename)[0] if 'csv' in filename else filename
        self.df = pd.DataFrame()

    @staticmethod
    def change_wav_folder(folder_name):
        folder_name = re.sub(r'/$', '', folder_name)
        WitcherData.wav_folder = f'{folder_name}/'

    def read_file(self, tag=''):
        filename = f'{self.filename}_{tag}' if tag else self.filename
        # fillna incase of missing string(np.nan = float), for filter step
        self.df = pd.read_csv(f'{filename}.csv', encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE).fillna('')

    def save_file(self, tag='', export=False, index=False, header=False, mask_exp=''):
        df = self.df
        if mask_exp:
            df = df[eval(mask_exp)]
        if export:
            df = df[['Audio', 'Content', 'Processed']]
        filename = f'{self.filename}_{tag}' if tag else self.filename
        df.to_csv(f'{filename}.csv', encoding='utf-8', index=index, header=header, sep='|', quoting=csv.QUOTE_NONE)

    def check_audio(self):
        self.df['Exist'] = self.df['Audio'].parallel_apply(
            lambda audio: os.path.isfile(f'{WitcherData.wav_folder}{self.filename}/{audio}.wav'))

    def get_audio_length(self):
        self.df['Duration'] = self.df['Audio'].parallel_apply(
            lambda audio: librosa.get_duration(filename=f'{WitcherData.wav_folder}{self.filename}/{audio}.wav'))

    def analyze_text(self):
        self.df[
            'Processed'
        ], self.df[
            'Attribute'
        ], self.df[
            'Count'
        ], self.df[
            'Syllables'
        ], self.df[
            'fasttext'
        ], self.df[
            'fasttext_processed'
        ], self.df[
            'cld2'
        ], self.df[
            'cld2_processed'
        ], self.df[
            'langdetect'
        ], self.df[
            'langdetect_processed'
        ] = list(zip(*self.df['Content'].parallel_apply(tag_and_process).to_list()))

    def filter_scene(self):
        """Scenes to be filtered out"""
        if self.filename == 'Geralt':
            # filter out those drunk scenes with unclear audio
            scenes = ['q401_06_04_reunion_part_02',
                      'q401_06_07_gmpl_finding_drunk_eskel',
                      'q401_06_08_found_drunk_eskel',
                      'q401_06_09_calling_ida_drunk']
            self.df = self.df[~self.df['Scene'].isin(scenes)]

    def filter_exist(self):
        self.df = self.df[self.df['Exist']]

    def filter_lang(self):
        is_eng = self.df.parallel_apply(
            lambda row: any(['en' in row[col] for col in ['fasttext',
                                                          'fasttext_processed',
                                                          'cld2',
                                                          'cld2_processed',
                                                          'langdetect',
                                                          'langdetect_processed']]),
            axis=1
        )
        self.df = self.df[is_eng]

    def drop_info(self):
        self.df.drop(['Speaker', 'Exist', 'ID'], axis=1, inplace=True)
