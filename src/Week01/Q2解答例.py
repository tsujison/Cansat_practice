a=str(input("A:じゃんけんの手札を入力してください："))
b=str(input("B:じゃんけんの手札を入力してください："))
if a==b:
    print("あいこです。")
elif(a=="グー" and b=="チョキ")\
    or(a=="チョキ" and b=="パー")\
    or(a=="パー" and b=="グー"):
    print("Aの勝ち")
else:
    print("Bの勝ち")