#台灣大樂透是一種數字開獎遊戲,每次樂透開獎時,會從 01~49 中任選 6 個號
#碼加 1 個特別號,並透過開獎號碼計算中獎人數與分配金額。在這 7 個號碼
#中,數字不能重複;且必須介於 01~49 數字區間。請設計一個程式,先輸入欲
#產生的樂透組數 N(1 < N <= 100),判斷各組所輸入的 7 組數字中,是否符合
#樂透號碼的標準;是的話,顯示 Yes;不是的話,則顯示 No。

N =eval(input())

for i in range(N):
    LS =input('').split(' ')
    CLS=[]
    for ls in LS:
        ils =int(ls)
        if (ils>=1 and ils<=49) and (ils not in CLS):
            CLS.append(ils)
        else:
            print('NO')
            break
    
    if len(CLS)==7:
        print('YES')
