    mov rax, qword ptr [rbp-0x3f80]	# src(main's argv)
    add rax, 0x8
    mov rsi, qword ptr [rax]
    lea rax, [rbp-0x3eb0]	# dst
    mov rdi, rax 
    mov rcx, 0x400FF0 #strcpy addr
    call rcx 

    lea rbx,[rbp-0x3eb0]	#str addr
    mov rcx, 0

    loopme:
    movzx eax, byte ptr [rbx]
    cmp al, 0x0
    jz myend
    inc rbx
    inc rcx
    jmp loopme

    myend:
    mov [rax], rcx	#rcx is len(str)

    lea rax, [rbp-0x20]
    mov rbx, 0x4013cf
    mov [rax], rbx
