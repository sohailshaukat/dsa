from collections import Counter, deque
import copy
import graphviz


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


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def grow(node):
    if node.get("chars"):
        left = grow(node["chars"][0])
        right = grow(node["chars"][1])

        return Node(value=node["count"], left=left, right=right)

    return Node(value=node["char"] + ": " + str(node["count"]))


def visualize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.value))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.value))
            dot.edge(str(node.value), str(node.left.value))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.value))
            dot.edge(str(node.value), str(node.right.value))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render("binary_tree", view=True, format="png")


def draw(tree):
    duplicate = copy.deepcopy(tree)

    root = duplicate.popleft()
    new_tree = grow(root)

    visualize_binary_tree(new_tree)


message = "BCCABBDDAECCBBAEDDCC"
stats(message)

count_table = Counter(message)
count_table = sorted(
    [{"char": char, "count": count_table[char]} for char in count_table],
    key=lambda el: el["count"],
)

tree = create_tree(count_table)
# draw(tree)
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
    if reverse_table.get("".join(key)):
        received_message_in_bytes.append(reverse_table["".join(key)])
        key = []

decoded_message = "".join(received_message_in_bytes)
print("Message received: ", decoded_message)
print("Is message same?: ", message == decoded_message)
