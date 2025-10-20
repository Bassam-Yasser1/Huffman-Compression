import heapq
import copy
from collections import Counter

class Node:
    def __init__(self, chars, prob, left=None, right=None):
        self.chars = chars
        self.prob = prob
        self.left = left
        self.right = right

    def __lt__(self, other): # operator overloading for "<"
        # Needed for heapq
        return self.prob < other.prob

    def __repr__(self): #how you represent Node object "May be used later"
        return f"Node(chars='{self.chars}', prob={self.prob:.4f})"

def get_frequencies(filename):
    with open(filename, 'r', encoding='utf-8') as f: # 'r' is read mode 
        text = f.read()

    freq = Counter(text) #freq is a subtype of dictionary "Collections.Counter"
    total = sum(freq.values())
    
    probabilities = {ch: freq[ch] / total for ch in freq}

    return freq, probabilities

# Build Huffman Tree
def huffman(probabilities):
    # Initialize heap with leaf nodes
    heap = [Node(ch, prob) for ch, prob in probabilities.items()] # fill the heap with the nodes
    heapq.heapify(heap)

    # To track all stages of merging
    stages = [copy.deepcopy(heap)]

    while len(heap) > 1: 
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.chars + right.chars, left.prob + right.prob, left, right)
        heapq.heappush(heap, merged)

        stages.append(copy.deepcopy(heap))

    root = heap[0]
    return root, stages

def assign_codes(node, code='', codes=None):
    if codes is None:
        codes = {}

    if node.left is None and node.right is None:
        codes[node.chars] = code
        return codes

    if node.left:
        assign_codes(node.left, code + '1', codes)
    if node.right:
        assign_codes(node.right, code + '0', codes)

    return codes

def huffman_from_file(filename):
    freq, probabilities = get_frequencies(filename)

    print("Character Frequencies:")
    for ch, f in freq.items():
        print(f"'{ch}': {f}")

    root, stages = huffman(probabilities)
    codes = assign_codes(root)

    print("\nHuffman Codes:")
    for ch, code in codes.items():
        print(f"'{ch}': {code}")

    return freq, probabilities, stages, codes

def compress(filename,codes):
    with open(filename, 'r', encoding='utf-8') as f: 
        text = f.read()
    
    for ch in text:
       text = text.replace(ch,codes[ch])
    return text

def saveAsBin(text):
    # Ensure the length is a multiple of 8 bits (pad with zeros if needed)
    padding = 8 - len(text) % 8
    if padding != 8:
        text += '0' * padding

    # Convert binary string to bytes
    b = bytearray()
    for i in range(0, len(text), 8):
        byte = text[i:i+8]
        b.append(int(byte, 2))

    with open("compressed.bin", "wb") as f:
        f.write(b)



if __name__ == "__main__":
    filename = input("Enter filename to compress ")
    freq, probs, stages, codes = huffman_from_file(filename)

    # print("\nStages of merging:")
    # for i, stage in enumerate(stages):
    #     print(f"Stage {i}: {stage}")

    text = compress(filename,codes)
    print()
    print(text)
    
    saveAsBin(text)