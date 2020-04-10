# SM4701 SIU KING WAI 54412743
from util import WitcherData, get_parameter


if __name__ == '__main__':
    data = WitcherData(get_parameter())
    data.read_file(tag='processed')
    # all
    data.save_file('all', export=True)
    # without question
    data.save_file('no_q', export=True,
                   mask_exp="~df['Attribute'].str.contains('Q')")
    # without exclamation
    data.save_file('no_e', export=True,
                   mask_exp="~df['Attribute'].str.contains('E')")
    # without both
    data.save_file('no_qe', export=True,
                   mask_exp="~(df['Attribute'].str.contains('Q') | df['Attribute'].str.contains('E'))")
    # all at least 3 words
    data.save_file('s3', export=True,
                   mask_exp="df['Syllables'] >= 3")
    # all at least 5 words
    data.save_file('s5', export=True,
                   mask_exp="df['Syllables'] >= 5")
    # all at least 9 words
    data.save_file('s9', export=True,
                   mask_exp="df['Syllables'] >= 9")

    print('Filter done')
