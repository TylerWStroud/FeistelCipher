# Feistel Cipher
Named after Horst Feistel, the Feistel Cipher incorporates a symmetric key infrastructure where the key is known only by the sender and receiver.
This is a simplified, more digestible version for practical demonstration purposes.

### How it works
The cipher works in "rounds", or iterations. This demonstration only works in 2 rounds.

The logic is as follows
```
Step 1: The function takes as input 8 bits and the 4-bit key k. 
Step 2: The binary is divided into two halves (L_0 and R_0). 
Step 3: The function computes L_1=R_0 and R_1=L0⊕F(R_0,k), where F(R_0,k)=2×R_0^k  mod 2^4  
Step 4: The function performs a swapping of L_1 and R_1, then outputs R_1 ||L_1. 
```
### How to use it
Run the Python file in your IDE of choice. You will be prompted by a menu for further interaction with the algorithm.
