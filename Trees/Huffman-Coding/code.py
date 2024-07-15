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
reverse_table = {table[key]: key for key in table}

substituted_message = "".join([table[char] for char in message])
print("New Size of message: ", len(substituted_message))
m_table = "".join([bin(ord(key))[2:].zfill(8) + str(table[key]) for key in table])
print("Size of table: ", len(m_table))


received_message = deque(substituted_message)
received_message_in_bytes = []

key = []
while received_message:
    key.append(received_message.popleft())
    if reverse_table.get(''.join(key)):
        received_message_in_bytes.append(reverse_table[''.join(key)])
        key = []
    
decoded_message = "".join(received_message_in_bytes)
print("Message received: ", decoded_message)
print("Is message same?: ", message == decoded_message)