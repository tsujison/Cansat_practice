def fib_sequence(n: int) -> list:
    """
    長さ n のフィボナッチ列をリストで返す（再帰実装）。
    例: n=5 -> [0, 1, 1, 2, 3]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    prev = fib_sequence(n - 1)        # 再帰呼び出し
    prev.append(prev[-1] + prev[-2])  # 最後の2項の和を追加
    return prev

if __name__ == "__main__":
    k = int(input("出力するフィボナッチ数の個数 n を入力してください: "))
    seq = fib_sequence(k)
    print(seq)


#１：def fib_sequence(n: int) ->list:
#(n:int):引数を表す。ｎに整数intを渡す。pythonでは型ヒントと呼ばれる。
#->list 戻り値（返す値）の型ヒント。「この関数はlistを返すつもりである」を表す。

#２：prev=fib_sequence(n-1)
#ここが再帰呼び出しにあたる。再帰呼び出しとは、関数の中で自分自身をもう一度呼び出すことである。
#具体的な流れ
#fib_sequence(5)を呼ぶと、中でfib_sequence(4)を呼び出す。
#更にfib_sequence(4)はfib_sequence(3)を呼ぶ
#こうして、nが２になるまで繰り返される形になる。

#３：prev.append(prev[-1]+prev[-2])
#この行でフィボナッチ数列の次の項を追加している。
#prev[-1]          :リストから最後の要素
#prev[-2]          :最後から二番目の要素
#prev[-1]+prev[-2] :「最後の二項の和」->フィボナッチ数列の増え方
#.append           :リストの末尾に新しい値を追加する。

#４：if __name__=="__main__"
#「このファイルを直接じっくした時だけ、この中のコードを動かす」という意味。

#直接実行          ⇒ __name__ は "__main__"
#importされた時    ⇒ __name__ は "ファイル名"　　になる。
#要するにこれの下にあるコードは「このファイルを直接実行したときだけ動くようにする」仕組みである

#５：seq=fib_sequence(k)
#入力した個数kを使って関数を実際に呼び出している
#fib_sequence(k)に渡すとフィボナッチ数列（リスト）が返ってくる
#その結果をseqに格納する
