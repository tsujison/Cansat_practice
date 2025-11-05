while True:
    print("1はグー、2はチョキ、3はパーです。")
    a=int(input("A:1・2・3のいずれかを入力："))
    b=int(input("B:1・2・3のいずれかを入力："))
    if a==1 and b==1:
        print("あいこです。")
    elif a==2 and b==1:
        print("Bの勝ちです。")
    elif a==3 and b==1:
        print("Aの勝ちです。")
    elif a==1 and b==2:
        print("Aの勝ちです。")
    elif a==2 and b==2:
        print("あいこです。")
    elif a==3 and b==2:
        print("Bの勝ちです。")
    elif a==1 and b==3:
        print("Bの勝ちです。")
    elif a==2 and b==3:
        print("Aの勝ちです。")
    elif a==3 and b==3:
        print("あいこです。")   



