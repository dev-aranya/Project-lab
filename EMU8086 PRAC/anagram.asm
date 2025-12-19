.model small
.stack 100h

.data
str1 db "listen$",0
str2 db "silent$",0

len1 dw 0
len2 dw 0

msgTrue  db "True$",0
msgFalse db "False$",0

.code
main proc
    mov ax, @data
    mov ds, ax

; -------- Length of str1 --------
    lea si, str1
    xor cx, cx
len1_loop:
    cmp byte ptr [si], '$'
    je len1_done
    inc cx
    inc si
    jmp len1_loop
len1_done:
    mov len1, cx

; -------- Length of str2 --------
    lea si, str2
    xor cx, cx
len2_loop:
    cmp byte ptr [si], '$'
    je len2_done
    inc cx
    inc si
    jmp len2_loop
len2_done:
    mov len2, cx

; -------- Compare lengths --------
    mov ax, len1
    cmp ax, len2
    jne not_anagram

; -------- Sort str1 --------
    mov cx, len1
    dec cx
outer1:
    lea si, str1
    mov dx, cx
inner1:
    mov al, [si]
    mov bl, [si+1]
    cmp al, bl
    jbe skip1
    mov [si], bl
    mov [si+1], al
skip1:
    inc si
    dec dx
    jnz inner1
    loop outer1

; -------- Sort str2 --------
    mov cx, len2
    dec cx
outer2:
    lea si, str2
    mov dx, cx
inner2:
    mov al, [si]
    mov bl, [si+1]
    cmp al, bl
    jbe skip2
    mov [si], bl
    mov [si+1], al
skip2:
    inc si
    dec dx
    jnz inner2
    loop outer2

; -------- Compare strings --------
    lea si, str1
    lea di, str2
    mov cx, len1

compare_loop:
    mov al, [si]
    cmp al, [di]
    jne not_anagram
    inc si
    inc di
    loop compare_loop

; -------- Anagram --------
    mov dx, offset msgTrue
    mov ah, 9
    int 21h
    jmp exit

not_anagram:
    mov dx, offset msgFalse
    mov ah, 9
    int 21h

exit:
    mov ah, 4Ch
    int 21h
main endp
end main
