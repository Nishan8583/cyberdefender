flag = [0x6d,0x78,0x61,0x6c,0xdd,0x7e,0x65,0x7e,0x47,0x6a,0x4f,0xcc,0xf7,0xca,0x73,0x68,0x55,0x42,0x53,0xdc,0xd7,0xd4,0x6b,0xec,0xdb,0xd2,0xe1,0x1c,0x6d,0xde,0xd1,0xc2]
decrypted = []
encrypte_message = "my message"
input_was= []
for i in range(0,len(encrypte_message)-1):
    input_was.append(ord(encrypte_message[i]))
    value = ((i % 0xFF) | 0xA0) ^ ((2 * ord(encrypte_message[i])) | 1)
    # 110
    # 220
 # (orignal value + 1) 
    decrypted.append(value)
print(input_was)
print("encrypted",decrypted)
out = []
for i in range(0,len(decrypted)-1):
    input_was.append(decrypted[i])
    value = ((i % 0xFF) | 0xA0) ^ ((2 * decrypted[i]) | 1)
 
    out.append(value)
print(decrypted)

def decrypt(encrypted):
    d = ""
    for i in range(0,len(encrypted)):
        operator = ((i % 0xFF) | 0xA0)
        value = int(operator ^ (encrypted[i]))
        value = int((int(value) | 1)/ 2)
        print(value)
        d = d + chr(value)

    print(d)
decrypt(flag)
