#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import time
import marisa_trie   # 静态
import datrie        # 动态
if __name__ == '__main__':
    # marisa_trie 举例
    start = time.time()
    with open('data\qq.txt', 'r') as f:
        trie = marisa_trie.Trie([line.strip() for line in f])   # 只可以一次性导入，但是快
    trie.save(r'data/trie.marisa')
    trie = marisa_trie.Trie()
    trie.load(r'data/trie.marisa')
    print('86269383' in trie)
    print(time.time() - start)


    # datrie 举例
    start = time.time()
    trie = datrie.Trie(string.digits)
    with open('data\qq.txt', 'r') as f:
        for line in f:
            trie[line.strip()] = True                           # 可以多次导入，但是超级慢
    trie.save(r'data/trie.datrie')
    trie = datrie.Trie.load(r'data/trie.datrie')
    print('86269383' in trie)
    print(time.time()-start)