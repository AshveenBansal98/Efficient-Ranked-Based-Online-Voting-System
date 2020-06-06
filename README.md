# Efficient-Ranked-Based-Online-Voting-System
Efficient Ranked Based Online Voting System based on Homomorphic Encryption.
There can be multiple clients, which send the encrypted form of user vote to server. Server performs addition over the encrypted vote vectors (as encryption is homomorphic, we need not decrypt the cipher to perform addition). The server tells total vote count when 0 is pressed.
