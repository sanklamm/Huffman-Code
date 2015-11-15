#! /usr/bin/env python3
from sys import stdin

string = ''
# Class Node Tree
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


#builds binary codes for each character by traversing the Huffman tree
def huffman(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman(l, True, binString + "0"))
    d.update(huffman(r, False, binString + "1"))
    return d

for line in stdin:
    temp = line.split(',')
    string = temp[0]
    code = temp[1].strip()

    # builds a dictionary with the frequency of each character
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1


    # sort the dictionary by frequency --> builds tupels
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    nodes = freq

    #builds the Huffman tree from the frequency table
    while len(nodes) > 1:
        key1, c1 = nodes[-1]
        key2, c2 = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        # sorts the list again
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    # saves the Huffman Code as a dict
    huffmanCode = huffman(nodes[0][0])

    # Decodes the given code and buids the output.
    output = ''
    while code != "":
        for char, frequency in freq:
            if code.startswith( huffmanCode[char] ):
                output = output + char
                code =  code[len(huffmanCode[char]):]

    print(output)