# trie
- A trie is also known as a radix tree. In a normal radix tree, a key is the actual path taken through the tree to get to the corresponding value. 
- There are also no key collisions in a trie, like there might be in hash-tables.
- They can, however, be rather inefficient, like when you have a long key where no other key shares a common prefix. Then you have to travel (and store) a considerable number of nodes in the tree to get to the value.

# ethereum modification of trie
The ethereum implementation of radix trees introduces a number of improvements. First, to make the tree cryptographically secure, each node is referenced by its hash, which in current implementations are used for look-up in a leveldb database. With this scheme, the root node becomes a cryptographic fingerprint of the entire data structure (hence, Merkle). Second, a number of node ‘types’ are introduced to improve efficiency. There is the blank node, which is simply empty, and the standard leaf node, which is a simple list of [key, value]. Then there are extension nodes, which are also simple [key, value] lists, but where value is a hash of some other node. The hash can be used to look-up that node in the database. Finally, there are branch nodes, which are lists of length 17. The first 16 elements correspond to the 16 possible hex characters in a key, and the final element holds a value if there is a [key, value] pair where the key ends at the branch node. 

One more important thing is a special hex-prefix (HP) encoding used for keys. As mentioned, the alphabet is hex, so there are 16 possible children for each node. Since there are two kinds of [key, value] nodes (leaf and extension), a special ‘terminator’ flag is used to denote which type the key refers to. If the terminator flag is on, the key refers to a leaf node, and the corresponding value is the value for that key. If it’s off, then the value is a hash to be used to look-up the corresponding node in the db. HP also encodes whether or not the key is of odd or even length. Finally, we note that a single hex character, or 4 bit binary number, is known as a nibble.

The HP specification is rather simple. A nibble is appended to the key that encodes both the terminator status and parity. The lowest significant bit in the nibble encodes parity, while the next lowest encodes terminator status. If the key was in fact even, then we add another nibble, of value 0, to maintain overall evenness (so we can properly represent in bytes).