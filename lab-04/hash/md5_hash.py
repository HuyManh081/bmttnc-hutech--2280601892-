# lab-04 > hash > md5_hash.py

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    original_length = len(message) # Độ dài ban đầu của tin nhắn (bytes)
    message += b'\x80' # Thêm bit '1' theo quy ước padding MD5

    # Thêm các bit '0' cho đến khi độ dài là 448 mod 512
    # Đây là bước quan trọng: bạn cần thêm 0x00 bytes, không phải 0x80 bytes lặp lại
    while (len(message) * 8) % 512 != 448:
        message += b'\x00' # Thay đổi từ b'\x80' sang b'\x00'

    # Thêm độ dài ban đầu của tin nhắn (64 bit - Little Endian)
    message += original_length.to_bytes(8, 'little')

    # Bảng T (hằng số) - Di chuyển lên trước vòng lặp chính
    T = [
        0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
    ]

    # Shift amounts - Di chuyển lên trước vòng lặp chính
    s = [
        [7, 12, 17, 22],
        [5, 9, 14, 20],
        [4, 11, 16, 23],
        [6, 10, 15, 21]
    ]

    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        a0, b0, c0, d0 = a, b, c, d
        
        for j in range(64):
            if j < 16:
                F = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                F = (d & b) | ((~d) & c)
                g = (5*j + 1) % 16
            elif j < 48:
                F = b ^ c ^ d
                g = (3*j + 5) % 16
            else:
                F = c ^ (b | (~d))
                g = (7*j) % 16
            
            temp = d
            d = c
            c = b
            
            b = left_rotate((a + F + words[g] + T[j]) & 0xFFFFFFFF, s[j//16][j%4]) + b
            b &= 0xFFFFFFFF 
            a = temp

        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    # Kết quả cuối cùng (digest)
    # Chuyển đổi các biến a, b, c, d thành chuỗi byte little-endian và nối lại
    digest = a.to_bytes(4, 'little') + \
             b.to_bytes(4, 'little') + \
             c.to_bytes(4, 'little') + \
             d.to_bytes(4, 'little')

    return digest.hex() # Trả về dạng chuỗi hex

input_string = input("Nhap chuoi can bam: ")
md5_hash = md5(input_string.encode('utf-8'))

print("Ma bam MD5 cua chuoi '{}' la: {}".format(input_string, md5_hash))