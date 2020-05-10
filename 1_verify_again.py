# SIU KING WAI SM4701 Deepstory
from util import WitcherData, get_parameter


if __name__ == '__main__':
    data = WitcherData(get_parameter())
    data.read_file()
    data.check_audio()
    # data.check_audio_from_df()
    data.save_file(header=True)
    print('Verify done.')
