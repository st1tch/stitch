_start:

filename:
	xor esi, esi
	mul esi

	push rdx

	mov rcx, 0x73695f736968742f
	push rcx

	mov rcx, 0x2f2f2f2f2f2f2f2e
	push rcx

openfile:
	push rsp
	pop rdi

	mov al, 0x2
	syscall

readfile:
	push rax
	pop rdi

	push rsp
	pop rsi

	push rdx
	push rdx
	push rdx
	push rdx
	pop rax
	mov dx, 0x999
	syscall

write:
	pop rdi
	inc edi

	push rax
	pop rdx
	pop rax
	inc eax
	syscall

leave:
	pop rax
	mov al, 60
	syscall
