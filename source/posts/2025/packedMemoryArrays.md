---
tags: sphinx
date: "2025-05-31"
category: "Data structures"
---
# Packed Memory Arrays

A common problem, is I have a collection of data to keep in sorted order, but are going to regularly insert and remove elements. I care about how this performs at scale, so what data structure do I use? Some flavor of tree structure is great and flexible, but data is spread wide so doesn't perform great. A flat a array would be ideal in terms of storage, but insertion and deletion require a lot of data movement. 

I caught a interesting talk from Brian Wheatman and Helen Xu, and they had presented the very clever solution called a Packed-Memory-Array or PMA for short. The idea here is allocate a single over-sized array, and manage local dense sections with a tree-like structure. Insertion and deletion become easy with fairly small amount of data movement required to rebalance. But walking is not comparable to that of the flat array.

Check out their code on github https://github.com/wheatman/Packed-Memory-Array
