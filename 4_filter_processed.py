# SIU KING WAI SM4701 Deepstory
""" For edited script after checking combined audio"""
from util import WitcherData, get_parameter

if __name__ == '__main__':
    data = WitcherData(get_parameter())
    data.read_file(tag='processed')
    data.check_audio()
    data.filter_exist()
    data.save_file(tag='processed', header=True)
    print('done.')
