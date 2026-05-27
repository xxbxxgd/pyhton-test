#有一位作文老師不喜歡學生使用太長的字來寫文章,請幫忙老師判斷學生寫的
#句子是否包含長字串(longWord)。longWord 的定義是連續的字元,即英文字
#母: A~Z 或 a~z 所組成的字而且字母個數大於等於 10。
#例如: Kindergarden 為長字串,因為它有 12 個字母,但 hot 則不為長字串,
#因為它僅有 3 個字母。
#Input:輸入的第一列會有一個整數 T(1 <= T <= 200)表示測試資料的筆數。
#測試資料每筆一行,每行至少有一個字,不論長短,即可能為長字串但也可能
#不是。字與字之間以空格隔開。
#Output:輸出每一行長字串(longWord)的個數。

#輸入範例: 輸出範例:
#7 
#Meeeeeeeep Meeeeeeeep Meeeep meeeep                            2
#Minneapolis is a beautiful city                                1
#Spring is the pleasant time among four seasons.                0
#Shsssssssssh I am hunting                                      1
#Once upon a time                                               0
#Intelligent person are undemanding people                      2
#Photography require imagination and inspiration personality    4

N = eval(input())
for i in range(N):
    LS = input().split(' ')
    CT =0
    for ls in LS:
        if len(ls) >= 10:
            CT += 1
    
    print(CT)