 INCLUDE 'EMU8086.INC'

.MODEL SMALL
.STACK 100H
.CODE
.DATA   

MAIN PROC
    PRINT 'ENTER FIRST NUMBER :'
    MOV AH,01H
    INT 21H
    
    MOV BL,AL
    SUB BL,48
    
    MOV DL,10
    MOV AH,02H
    INT 21H
    
    MOV DL,13
    MOV AH,02H
    INT 21H
    
    
    PRINT 'ENTER SECOND NUMBER:'
    MOV AH,01H
    INT 21H
    SUB AL,48
    
    MUL BL
    
    MOV BL,AL
    ADD BL,48
    
     MOV DL,10
    MOV AH,02H
    INT 21H
    
    MOV DL,13
    MOV AH,02H
    INT 21H
    
    PRINT 'PRODUCT:'
    MOV DL,BL
    MOV AH,02H
    INT 21H
    
    MAIN ENDP
END MAIN