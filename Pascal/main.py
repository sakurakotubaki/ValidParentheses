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
generate_pascal_triangle(5)