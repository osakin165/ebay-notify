import pandas as pd

def load_wantlist(filepath='ebayプログラム用want list.xlsx'):
    df = pd.read_excel(filepath)
    df = df.dropna(subset=['ARTIST', 'TITLE'])  # 空行を除外

    wantlist = []
    for _, row in df.iterrows():
        wantlist.append({
            'artist': str(row['ARTIST']).strip(),
            'title': str(row['TITLE']).strip()
        })
    return wantlist
