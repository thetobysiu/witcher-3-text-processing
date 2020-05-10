# SIU KING WAI SM4701 Deepstory
from util import WitcherData, get_parameter


if __name__ == '__main__':
    data = WitcherData(get_parameter(), parallel=True)
    data.read_file()
    data.filter_exist()
    # data.filter_scene()
    # data.get_audio_length()
    data.drop_info()
    data.analyze_text()
    # data.filter_lang()
    data.save_file(tag='processed', header=True)
    print('Preprocess done.')
