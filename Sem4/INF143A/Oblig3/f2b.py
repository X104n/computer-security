def bytes_to_bits(B):
    bits = []
    for i in range(len(B)):
        current_byte = B[i]
        mask = 128
        for j in range(8):
            if (current_byte >= mask):
                bits.append(1)
                current_byte -= mask
            else:
                bits.append(0)
            mask = mask // 2
    return bits


def bits_to_bytes(B):
    byteseq = []
    num_bytes = len(B) // 8
    assert 8 * num_bytes == len(B)
    for i in range(num_bytes):
        current_byte = 0
        bit_sequence = B[(i * 8):((i + 1) * 8)]
        mask = 128
        for j in range(8):
            current_byte += mask * bit_sequence[j]
            mask = mask // 2
        byteseq.append(current_byte.to_bytes(1, "big"))
    return byteseq


def write_file(output_file, byteseq):
    f = open(output_file, "wb")
    for i in range(len(byteseq)):
        f.write(byteseq[i])
    f.close()


def read_file(input_file):
    f = open(input_file, "rb")
    data = f.read()
    f.close()
    return data


def readMain(file12):
    byteseq = read_file(file12)
    bitseq = bytes_to_bits(byteseq)
    return (bitseq)


def writeMain(fileName, bitseq):
    byteseq = bits_to_bytes(bitseq)
    write_file(fileName, byteseq)
