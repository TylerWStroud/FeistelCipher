def Feistel_Cipher(data, k, decrypt=False):
    def Feistel_Cipher_Binary(bits, k, decrypt=False):
        L0 = int(bits[:4], 2)
        R0 = int(bits[4:], 2)
        k = int(k, 2)

        # encryption function
        def F(R0_bits, key):
            return (2 * (R0_bits ** key)) % 16

        if not decrypt:
            # Encryption (same as original)
            L1 = R0
            R1 = L0 ^ F(R0, k)
        else:
            # Decryption (reverse operation)
            R1 = L0
            L1 = R0 ^ F(L0, k)

        return format(L1, '04b') + format(R1, '04b')

    output = ''
    for e in data:
        if e in '01':
            output = Feistel_Cipher_Binary(data, k, decrypt)
            break
        else:
            bits = format(ord(e), '08b')  # Using 8 bits for proper character handling
            # Process as two 4-bit halves
            first_half = Feistel_Cipher_Binary(bits[:4] + bits[4:8], k, decrypt)
            e_char = chr(int(first_half, 2))
            output += e_char
    return output

if __name__ == "__main__":
    while True:
        print("\n======== FEISTEL CIPHER ========\n\n"
              "This is a simplified demonstration of the Feistel Cipher.\n\n"
              "You will be prompted to input a single string (word), or an 8-bit binary value.\n"
              "Then you will be prompted for a key (4-bit binary value)")

        user_input = input("\nBegin (Y/N)?: ").strip().upper()
        if user_input == 'Y':
            plain_text = input("\nEnter your message to be encrypted/decrypted (string or binary): ")
            operation = input("Encrypt (E) or Decrypt (D)?: ").strip().upper()
            key = input("Enter your key (4-bit binary): ")
            
            if operation == 'E':
                result = Feistel_Cipher(plain_text, key)
                print(f"\nEncryption result:")
                decrypted = Feistel_Cipher(result, key, decrypt=True)
                print(f"\nRound-trip verification: {decrypted == plain_text}")
            elif operation == 'D':
                result = Feistel_Cipher(plain_text, key, decrypt=True)
                print(f"\nDecryption result:")
            else:
                print("Invalid operation choice!")
                continue
            
            if all(c in '01' for c in plain_text):
                print(f"Binary value: {plain_text}")
                print(f"Key: {key}")
                print(f"Output: {result}")
            else:
                print(f"Plaintext: {plain_text}")
                print(f"Key: {key}")
                print(f"Output: {result}")
                
                
                    
        elif user_input == 'N':
            print("\nEnd program.\n")
            break