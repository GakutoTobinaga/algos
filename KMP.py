def KMP_search(text, pattern):
    # 部分一致テーブルの作成
    lps = [0] * len(pattern)
    computeLPSArray(pattern, lps)
    
    i = 0 # textのインデックス
    j = 0 # patternのインデックス
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            print("パターンはテキストの位置 {} で見つかりました。".format(i-j))
            j = lps[j-1] # 次の一致を探すためにシフト
        
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pattern, lps):
    length = 0 # 最長共通接頭辞の長さ
    lps[0] = 0 # LPS[0]は常に0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
        # "ABCDA"現時点で一番長い部分と、次に調べたい部分を比較pattern[現時点での最長...]
            length += 1
            # 合っていた。ので最長を更新
            lps[i] = length
            # lpsに最長を記録。かつ、後々不一致が起きた時にシフト用として使うので記録する
            i += 1
            # 次の文字へ行くためにiを+1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                # 合ってないし、現時点で最長は０なのでそのまま記録
                i += 1
                # iを増やして次へ