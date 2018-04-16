#!/usr/bin/env python
# -*- coding: utf-8 -*-

# %%
import pickle
import time
import sys
import pandas
class TrieNode:
    '''
    Parameters
    ----------
    next : dict
        包含所有集结点
    flag : boolean
        记录该字符串是否存在
    '''
    # next = {}
    # flag = False
    def __init__(self):
        self.next = {}
        self.flag = False

class Trie:
    # root = TrieNode()
    def __init__(self):
        self.root = TrieNode()

    def insert(self,s):
        node = self.root
        for c in s:
            if c not in node.next:    # 如果该字节不在子节点中，就创建
                node.next[c] = TrieNode()
            node = node.next[c]
        else:
            node.flag = True

    def search(self,s):
        node = self.root
        for c in s:
            if c not in node.next:
                return False
            node = node.next[c]
        else:
            return node.flag
if __name__ == '__main__':
    trie = Trie()

    with open('data\qq.txt','r') as f:
        for line in f:
            trie.insert(line.strip())
    print(sys.getsizeof(trie))

    # 持久化trie树，方便下次运行
    with open(r'data\trie.pkl', 'wb') as f:
        pickle.dump(trie,f)
    del trie
    # 加载磁盘上的trie树
    with open(r'data\trie.pkl', 'rb') as f:
        trie = pickle.load(f)
    start = time.time()
    print(trie.search('18503629'))
    print(time.time()-start)
