from trie import Trie
from compressed_trie_4 import CompressedTrie4

t = CompressedTrie4()
# t.insertWord('see')
# t.insertWord('bear')
# t.insertWord('sell')
# t.insertWord('stock')
# t.insertWord('bull')
# t.insertWord('buy')
# t.insertWord('bid')
# t.insertWord('hear')
# t.insertWord('bell')
# t.insertWord('stop')

# # lev 1
# print("---Livello 1---")
# for i in t._root._children:
#     print(i)

# # lev 2
# print("---Livello 2---")
# for i in t._root._children['s']._children:
#     print(i)
# for i in t._root._children['b']._children:
#     print(i)
# for i in t._root._children['hear$']._children:
#     print(i)

# # lev 3
# print("---Livello 3---")
# for i in t._root._children['s']._children['e']._children:
#     print(i)
# for i in t._root._children['s']._children['to']._children:
#     print(i)
# for i in t._root._children['b']._children['e']._children:
#     print(i)
# for i in t._root._children['b']._children['u']._children:
#     print(i)
# for i in t._root._children['b']._children['id$']._children:
#     print(i)

# t = Trie()
t.insertWord('bear')
t.insertWord('bell')
t.insertWord('bid')
t.insertWord('bull')
t.insertWord('buy')
t.insertWord('sell')
t.insertWord('stock')
t.insertWord('stoppati')
t.insertWord('stop')
t.printTrie()
# # lev 1
# print("---Livello 1---")
# for i in t._root._children:
#     print(i)

# # lev 2
# print("---Livello 2---")
# for i in t._root._children['b']._children:
#     print(i)
# print('---')
# for i in t._root._children['s']._children:
#     print(i)

# # lev 3
# print("---Livello 3---")
# for i in t._root._children['b']._children['e']._children:
#     print(i)
# print('---')
# for i in t._root._children['b']._children['id$']._children:
#     print(i)
# print('---')
# for i in t._root._children['b']._children['u']._children:
#     print(i)
# print('---')
# for i in t._root._children['s']._children['ell$']._children:
#     print(i)
# print('---')
# for i in t._root._children['s']._children['to']._children:
#     print(i)

# # lev 4
# print("---Livello 4---")
# for i in t._root._children['s']._children['to']._children['p']._children:
#     print(i)
