#Build Huffman Tree

# def huffman(probabilities):
#     # Initialize heap with leaf nodes
#     heap = [Node(ch, prob) for ch, prob in probabilities.items()]
#     heapq.heapify(heap)

#     # To track all stages of merging
#     stages = [copy.deepcopy(heap)]

#     while len(heap) > 1:
#         left = heapq.heappop(heap)
#         right = heapq.heappop(heap)
#         merged = Node(left.chars + right.chars, left.prob + right.prob, left, right)
#         heapq.heappush(heap, merged)

#         stages.append(copy.deepcopy(heap))

#     root = heap[0]
#     return root, stages


# # ------------------------------
# # Step 3: Assign Huffman Codes
# # ------------------------------
# def assign_codes(node, code='', codes=None):
#     if codes is None:
#         codes = {}

#     if node.left is None and node.right is None:
#         codes[node.chars] = code
#         return codes

#     if node.left:
#         assign_codes(node.left, code + '0', codes)
#     if node.right:
#         assign_codes(node.right, code + '1', codes)

#     return codes


# # ------------------------------
# # Step 4: Full pipeline
# # ------------------------------
# def huffman_from_file(filename):
#     freq, probabilities = get_frequencies(filename)

#     print("Character Frequencies:")
#     for ch, f in freq.items():
#         print(f"'{ch}': {f}")

#     root, stages = huffman(probabilities)
#     codes = assign_codes(root)

#     print("\nHuffman Codes:")
#     for ch, code in codes.items():
#         print(f"'{ch}': {code}")

#     return freq, probabilities, stages, codes


# # ------------------------------
# # Example usage
# # ------------------------------
# if __name__ == "__main__":
#     filename = "input.txt"   # Replace with your text file path
#     freq, probs, stages, codes = huffman_from_file(filename)

#     # Example: inspect stages
#     print("\nStages of merging:")
#     for i, stage in enumerate(stages):
#         print(f"Stage {i}: {stage}")
