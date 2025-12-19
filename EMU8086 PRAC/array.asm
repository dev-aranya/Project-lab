  include 'emu8086.inc'
  .model small
  .stack 100h
  .data
    array db 2,3,4,6,1
  .code
     main proc
        mov ax,@data
        mov ds,ax
        
        mov si, offset array 
        mov cx,5
        
        print 'your array vlues:'
        
        loopx:
           
           mov dl,[si]     ;value
           add dl,48 
           
           mov ah,02h
           int 21h
           
           mov dl,32
           mov ah,02h      ;space
           int 21h
           
           inc si
           loop loopx
           
           mov ah,04ch
           int 21h
           
           main endp
     end main
           
          