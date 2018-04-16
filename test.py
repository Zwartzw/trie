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
        trie = marisa_trie.Trie([line.strip() for line in f])
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
            trie[line.strip()] = True
    trie.save(r'data/trie.datrie')
    trie = datrie.Trie.load(r'data/trie.datrie')
    print('86269383' in trie)
    print(time.time()-start)