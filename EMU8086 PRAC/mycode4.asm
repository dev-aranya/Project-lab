
include 'emu8086.inc'
.model small
.stack 100h
.code
.data

main proc  
    
    print 'enter character :'
    
    mov ah,01h
    int 21h
    
    mov bl,al
              
    
    mov dl,10          
    mov ah,02h
    int 21h
    
    mov dl,13
    mov ah,02h
    int 21h
    
    print 'Your character:'
    mov dl,bl
    
    mov ah,02h
    int 21h
    
    main endp
end main


