
.model small
.stack 100h

.data
num     dw 15
sum     dw 0

msgYes  db "Yes$",0
msgNo   db "No$",0

.code
main proc
    mov ax, @data
    mov ds, ax

    mov cx, 1            ; divisor = 1
    mov sum, 0

check_loop:
    mov ax, num
    cmp cx, ax
    jge done_check

    xor dx, dx
    div cx               ; AX / CX

    cmp dx, 0
    jne next_div

    add sum, cx

next_div:
    inc cx
    jmp check_loop

done_check:
    mov ax, sum
    cmp ax, num
    jne not_perfect

perfect:
    mov dx, offset msgYes
    mov ah, 9
    int 21h
    jmp exit

not_perfect:
    mov dx, offset msgNo
    mov ah, 9
    int 21h

exit:
    mov ah, 4Ch
    int 21h
main endp
end main




