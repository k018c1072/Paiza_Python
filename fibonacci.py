def fibonacci_func():
    """フィボナッチ数列を返す関数を返す メモイズ機能つき"""
    table = {}  # 計算済みのフィボナッチ数列を格納するテーブル

    def fibonacci(n):
        # 計算したことのある数値についてはテーブルを参照して返す
        if n in table:
            return table[n]

        # 計算したことのない数値についてはフィボナッチ数列の定義どおり計算
        if n < 2:
            return 1
        table[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return table[n]

    return fibonacci


# 関数を生成してから 50 番までのフィボナッチ数列を計算して表示する
f = fibonacci_func()
for i in range(50):
    print(f(i))
