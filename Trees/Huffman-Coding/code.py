from collections import Counter, deque


def ordered_insert(table, element, key="count"):
    for i, el in enumerate(table):
        if element[key] <= el[key]:
            table.insert(i, element)
            return
    else:
        table.append(element)


def create_tree(count_table):
    que = deque(count_table)
    while len(que) != 1:
        left = que.popleft()
        right = que.popleft()

        n = {"chars": (left, right), "count": left["count"] + right["count"]}

        ordered_insert(que, n, "count")
    return que


def create_table(tree, table, code=""):
    if tree[0].get("char"):
        table[tree[0]["char"]] = code + "0"
    else:
        create_table(tree[0]["chars"], table, code + "0")
    if tree[1].get("char"):
        table[tree[1]["char"]] = code + "1"
    else:
        create_table(tree[1]["chars"], table, code + "1")
    return table


def stats(message):
    message_binary = "".join([bin(ord(char))[2:].zfill(8) for char in message])

    print("Message: ", message)
    print("Message in binary: ", message_binary)
    print("Size of message: ", len(message_binary))


message = "BCCABBDDAECCBBAEDDCC"
stats(message)

count_table = Counter(message)
count_table = sorted(
    [{"char": char, "count": count_table[char]} for char in count_table],
    key=lambda el: el["count"],
)


tree = create_tree(count_table)
table = create_table(tree[0]["chars"], {})

substituted_message = "".join([table[char] for char in message])
print("sus", len(substituted_message))
m_table = "".join([bin(ord(key))[2:].zfill(8) + str(table[key]) for key in table])
print("pus", len(m_table))

final_message = substituted_message + m_table
