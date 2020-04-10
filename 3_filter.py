# SM4701 SIU KING WAI 54412743
from util import WitcherData, get_parameter


if __name__ == '__main__':
    data = WitcherData(get_parameter())
    data.read_file(tag='processed')

    df
    # all
    save_csv(df, 'all.csv')
    # without question
    save_csv(df[~df['Attribute'].str.contains('Q')], 'no_q.csv')
    # without exclamation
    save_csv(df[~df['Attribute'].str.contains('E')], 'no_e.csv')
    # without both
    save_csv(df[~(df['Attribute'].str.contains('Q') | df['Attribute'].str.contains('E'))], 'no_qe.csv')
    # all at least 3 words
    save_csv(df[df['Count'] >= 3], 'all3.csv')
    # all at least 5 words
    save_csv(df[df['Count'] >= 5], 'all5.csv')
    # all at least 10 words
    save_csv(df[df['Count'] >= 10], 'all10.csv')

    print('done')
