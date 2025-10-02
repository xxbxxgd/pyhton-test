while True:
    email = input("")
    
    if email == "0":
        break

    # 判斷條件 1: 必須包含 '@'
    if "@" not in email:
        print("False")
        continue

    # 判斷條件 2: 必須包含 '.'
    if "." not in email:
        print("False")
        continue

    # 判斷條件 3: '@' 前必須有文字或數字
    at_index = email.index("@")
    if at_index == 0:
        print("False")
        continue

    # 判斷條件 4: '.' 必須在 '@' 之後
    dot_index = email.rfind(".")
    if dot_index < at_index:
        print("False")
        continue

    # 所有條件符合，輸出 True
    print("True")
