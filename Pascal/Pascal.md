# パスカルの三角形
パスカルの三角形は以下のように再現できます：

```shell
                1
               1 1
              1 2 1
             1 3 3 1
            1 4 6 4 1
           1 5 10 10 5 1
          1 6 15 20 15 6 1
         1 7 21 35 35 21 7 1
        1 8 28 56 70 56 28 8 1
       1 9 36 84 126 126 84 36 9 1
```

## パスカルの三角形について
パスカルの三角形は、各数値が上の段の2つの数値の和になるという性質を持っています。各行は次の法則で作られます：
1. 最初と最後の数字は常に1
2. その他の数字は、真上の2つの数字の和

## Python でパスカルの三角形を生成するコード
パスカルの三角形をプログラムで生成する場合、以下のようなPythonコードが使えます：

```pycon
def generate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]  # 最初の要素は常に1
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # 最後の要素も常に1
        triangle.append(row)
    
    # 三角形を整形して表示
    for i, row in enumerate(triangle):
        print(' ' * (rows - i - 1) + ' '.join(map(str, row)))

# 10行のパスカルの三角形を生成
generate_pascal_triangle(10)
```

このコードを実行すると、上記のようなパスカルの三角形が表示されます。行数は任意に変更できます。
