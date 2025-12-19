.model small
.stack 100h

.data
n db 5          ; change n value here

.code
main proc
    mov ax, @data
    mov ds, ax

; ================= UPPER HALF =================
    mov cl, 1              ; line counter = 1

upper_loop:
    ; ----- print spaces -----
    mov bl, n
    sub bl, cl

space1:
    cmp bl, 0
    je inc_nums
    mov dl, ' '
    mov ah, 2
    int 21h
    dec bl
    jmp space1

    ; ----- print increasing numbers -----
inc_nums:
    mov bl, 1
inc_loop:
    cmp bl, cl
    ja dec_nums
    mov dl, bl
    add dl, '0'
    mov ah, 2
    int 21h
    inc bl
    jmp inc_loop

    ; ----- print decreasing numbers -----
dec_nums:
    mov bl, cl
    dec bl

dec_loop:
    cmp bl, 0
    je newline1
    mov dl, bl
    add dl, '0'
    mov ah, 2
    int 21h
    dec bl
    jmp dec_loop

newline1:
    mov dl, 13
    mov ah, 2
    int 21h
    mov dl, 10
    int 21h

    inc cl
    cmp cl, n
    jbe upper_loop

; ================= LOWER HALF =================
    mov cl, n
    dec cl

lower_loop:
    ; ----- print spaces -----
    mov bl, n
    sub bl, cl

space2:
    cmp bl, 0
    je inc_nums2
    mov dl, ' '
    mov ah, 2
    int 21h
    dec bl
    jmp space2

    ; ----- print increasing numbers -----
inc_nums2:
    mov bl, 1
inc_loop2:
    cmp bl, cl
    ja dec_nums2
    mov dl, bl
    add dl, '0'
    mov ah, 2
    int 21h
    inc bl
    jmp inc_loop2

    ; ----- print decreasing numbers -----
dec_nums2:
    mov bl, cl
    dec bl

dec_loop2:
    cmp bl, 0
    je newline2
    mov dl, bl
    add dl, '0'
    mov ah, 2
    int 21h
    dec bl
    jmp dec_loop2

newline2:
    mov dl, 13
    mov ah, 2
    int 21h
    mov dl, 10
    int 21h

    dec cl
    cmp cl, 0
    jne lower_loop

    mov ah, 4Ch
    int 21h
main endp
end main
