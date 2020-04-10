# SM4701 SIU KING WAI 54412743
from util import WitcherData, get_parameter


if __name__ == '__main__':
    data = WitcherData(get_parameter())
    data.read_file()
    data.check_audio()
    data.save_file(header=True)
    print('Verify done.')
