#豬式拉丁語(Pig Latin) 是一種英語語言遊戲,將英語字頭的字母調至字尾,
#再多加一個“ay”音節而成,如:“pig latin”變成“IGPAY ATINLAY”。
#輸入格式:
#第一行輸入整數 k 代表有 k 組測資,1 ≤ kk ≤ 100,接下來有 k 行,每一行
#輸入一個訊息。(只有小寫英文字母及空白)。
#輸出格式:
#輸出 k 行,每一行輸出豬式拉丁語。輸出為大寫英文字母,空白不用替換。
#輸入範例: 輸出範例:
#3 

#pig latin                   IGPAY ATINLAY
#hello world                 ELLOHAY ORLDWAY
#the quick brown fox         HETAY UICKQAY ROWNBAY OXFAY
def PLatin(oS):
    rS =oS[1:] +oS[0] +'ay'
    return rS.upper()

N = eval(input())
for i in range(N):
    LS = input().split(' ')
    RV =""
    for ls in LS:
        if RV =="":
            RV = PLatin(ls)
        else:
            RV += (" " +PLatin(ls))
    
    print(RV)