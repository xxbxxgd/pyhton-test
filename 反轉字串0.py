a=int(input(""))
result=[]
for _ in range(a):

    # 讀取輸入字串
    text = input("")

    # 去掉最後可能存在的換行符號
    text = text.strip()

    # 將字串反轉
    reversed_text = text[::-1]

    # 在每個字元之間插入逗號
    output = ",".join(reversed_text)

    # 輸出結果
    result.append(output)

for x in result:
    print(x)
