# SIU KING WAI SM4701 Deepstory
from util import WitcherData, get_parameter

if __name__ == '__main__':
    data = WitcherData(get_parameter())
    data.read_file(tag='processed')

    # all
    data.save_file('all', export=True, export_dir='export')

    # all at least 3 words and no action *sniff*
    data.save_file(
        's3_no_a', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 3) & ~(df['Attribute'].str.contains('A')))")

    # all at least 3 words and no question no action
    data.save_file(
        's3_no_qa', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 3) & ~(df['Attribute'].str.contains('Q') | df['Attribute'].str.contains('A')))")

    # all at least 3 words and no exclamation no action
    data.save_file(
        's3_no_ea', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 3) & ~(df['Attribute'].str.contains('E') | df['Attribute'].str.contains('A')))")

    # all at least 3 words and no qeustion no exclamation no action
    data.save_file(
        's3_no_qea', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 3) & ~(df['Attribute'].str.contains('Q') | "
                 "df['Attribute'].str.contains('E') | df['Attribute'].str.contains('A')))")

    # all at least 5 words and no action *sniff*
    data.save_file(
        's5_no_a', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 5) & ~(df['Attribute'].str.contains('A')))")

    # all at least 5 words and no question no action
    data.save_file(
        's5_no_qa', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 5) & ~(df['Attribute'].str.contains('Q') | df['Attribute'].str.contains('A')))")

    # all at least 5 words and no exclamation no action
    data.save_file(
        's5_no_ea', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 5) & ~(df['Attribute'].str.contains('E') | df['Attribute'].str.contains('A')))")

    # all at least 5 words and no qeustion no exclamation no action
    data.save_file(
        's5_no_qea', export=True, export_dir='export',
        mask_exp="((df['Syllables'] >= 5) & ~(df['Attribute'].str.contains('Q') | "
                 "df['Attribute'].str.contains('E') | df['Attribute'].str.contains('A')))")

    print('Filter done')
