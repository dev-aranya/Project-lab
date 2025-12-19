include 'emu8086.inc'
.model small
.stack 100h
.data
.code

main proc
    
    mov dl,3
    mov bl,4
    
    cmp dl,bl
    
    je show 
        print 'both are not same'
        mov ah,04h
        int 21h
        
        show:
        print 'both are same'
        mov ah,04h
        int 21h
        
        main endp
end main
        