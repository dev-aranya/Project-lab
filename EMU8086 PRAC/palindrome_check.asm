
.model small
.stack 100h

.data
str db "LEVEL$",0
msgYes db "Palindrome$",0
msgNo  db "Not Palindrome$",0

.code
main proc
    mov ax, @data
    mov ds, ax

    lea si, str
    lea di, str

; ----- find end of string -----
find_end:
    cmp byte ptr [di], '$'
    je back
    inc di
    jmp find_end

back:
    dec di          ; point to last character

; ----- compare characters -----
check:
    cmp si, di
    jae palindrome

    mov al, [si]
    cmp al, [di]
    jne not_pal

    inc si
    dec di
    jmp check

palindrome:
    mov dx, offset msgYes
    mov ah, 9
    int 21h
    jmp exit

not_pal:
    mov dx, offset msgNo
    mov ah, 9
    int 21h

exit:
    mov ah, 4Ch
    int 21h
main endp
end main



