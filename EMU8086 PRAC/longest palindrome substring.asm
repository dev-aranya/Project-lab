.model small
.stack 100h

.data
str     db "cbbd$",0
len     dw 0
start   dw 0
maxlen  dw 1

.code
main proc
    mov ax, @data
    mov ds, ax

; ========== FIND STRING LENGTH ==========
    lea si, str
    xor cx, cx

len_loop:
    cmp byte ptr [si], '$'
    je len_done
    inc cx
    inc si
    jmp len_loop

len_done:
    mov len, cx

; ========== MAIN LOOP ==========
    xor cx, cx          ; cx = center index

center_loop:
    cmp cx, len
    jae print_result

; ---------- ODD LENGTH ----------
    mov si, cx
    mov di, cx

odd_expand:
    cmp si, 0
    jl odd_done
    cmp di, len
    jae odd_done

    mov al, str[si]
    cmp al, str[di]
    jne odd_done

    mov bx, di
    sub bx, si
    inc bx              ; length = di - si + 1

    cmp bx, maxlen
    jbe odd_continue

    mov maxlen, bx
    mov start, si

odd_continue:
    dec si
    inc di
    jmp odd_expand

odd_done:

; ---------- EVEN LENGTH ----------
    mov si, cx
    mov di, cx
    inc di

even_expand:
    cmp si, 0
    jl even_done
    cmp di, len
    jae even_done

    mov al, str[si]
    cmp al, str[di]
    jne even_done

    mov bx, di
    sub bx, si
    inc bx

    cmp bx, maxlen
    jbe even_continue

    mov maxlen, bx
    mov start, si

even_continue:
    dec si
    inc di
    jmp even_expand

even_done:
    inc cx
    jmp center_loop

; ========== PRINT RESULT ==========
print_result:
    mov si, start
    mov cx, maxlen

print_loop:
    mov dl, str[si]
    mov ah, 2
    int 21h
    inc si
    loop print_loop

    mov ah, 4Ch
    int 21h
main endp
end main
