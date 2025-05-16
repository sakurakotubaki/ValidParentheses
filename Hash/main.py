from string import ascii_letters

# P178を読む
# abcは、ascii_lettersの０番目、１番目、２番目
def my_hash_func(text):
    hash_num = 0
    for c in text:
        hash_num += ascii_letters.index(c)
    return hash_num

hash_val = my_hash_func("abc")
print(hash_val) # 3

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return f"Node({self.key}, {self.value})"

# ハッシュテーブルの実装
class MyHashTabel:

    def __init__(self):
        self.size = 100
        self.data = [None] * self.size

    def set(self, key, value):
        hash_key = my_hash_func(key) % self.size
        self.data[hash_key] = Node(key, value)

    def get(self, key):
        hash_key = my_hash_func(key) % self.size
        self.data[hash_key] = None

    def delete(self, key):
        hash_key = my_hash_func(key) % self.size
        self.data[hash_key] = None

    def __str__(self):
        result = ""
        for idx, node in enumerate(self.data):
            if node:
                result += str(idx) + ":" + str(node) + "\n"
            return result
        return None


my_map = MyHashTabel()
my_map.set("tanaka", "tanaka@example.com")
my_map.set("yamada", "yamada@example.com")
print(my_map)

mail = my_map.get("tanaka")
print("mail:", mail)