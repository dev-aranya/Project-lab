.model small
.stack 100h

.data
a dw 18
b dw 24
c dw 30

gcd dw ?
lcm dw ?

msg1 db "GCD = $"
msg2 db 13,10,"LCM = $"

.code
main proc
    mov ax, @data
    mov ds, ax

; -------- GCD of a and b --------
    mov ax, a
    mov bx, b

gcd_ab:
    cmp bx, 0
    je ab_done
    xor dx, dx
    div bx
    mov ax, bx
    mov bx, dx
    jmp gcd_ab

ab_done:
    mov gcd, ax

; -------- GCD with c --------
    mov bx, c

gcd_abc:
    cmp bx, 0
    je gcd_done
    xor dx, dx
    div bx
    mov ax, bx
    mov bx, dx
    jmp gcd_abc

gcd_done:
    mov gcd, ax

; -------- LCM = (a*b*c)/gcd --------
    mov ax, a
    mul b
    mul c
    mov bx, gcd
    div bx
    mov lcm, ax

; -------- Print GCD --------
    mov dx, offset msg1
    mov ah, 9
    int 21h

    mov ax, gcd
    add al, '0'
    mov dl, al
    mov ah, 2
    int 21h

; -------- Print LCM --------
    mov dx, offset msg2
    mov ah, 9
    int 21h

    mov ax, lcm
    mov bx, 10
    xor cx, cx

print_lcm:
    xor dx, dx
    div bx
    push dx
    inc cx
    cmp ax, 0
    jne print_lcm

print_digits:
    pop dx
    add dl, '0'
    mov ah, 2
    int 21h
    loop print_digits

    mov ah, 4Ch
    int 21h
main endp
end main
