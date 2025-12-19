.model small
.stack 100h

.data
str db "Assembly$",0
count db 0
msg db "Vowels = $"

.code
main proc
    mov ax, @data
    mov ds, ax

    lea si, str

next_char:
    mov al, [si]
    cmp al, '$'
    je show_result

    ; check uppercase vowels
    cmp al, 'A'
    je vowel
    cmp al, 'E'
    je vowel
    cmp al, 'I'
    je vowel
    cmp al, 'O'
    je vowel
    cmp al, 'U'
    je vowel

    ; check lowercase vowels
    cmp al, 'a'
    je vowel
    cmp al, 'e'
    je vowel
    cmp al, 'i'
    je vowel
    cmp al, 'o'
    je vowel
    cmp al, 'u'
    je vowel

    jmp skip

vowel:
    inc count

skip:
    inc si
    jmp next_char

show_result:
    mov dx, offset msg
    mov ah, 9
    int 21h

    mov dl, count
    add dl, '0'
    mov ah, 2
    int 21h

    mov ah, 4Ch
    int 21h
main endp
end main
