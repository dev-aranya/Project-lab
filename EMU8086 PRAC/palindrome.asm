.MODEL SMALL
.STACK 100H

.DATA
    MAX_LENGTH    DB 80
    ACTUAL_LENGTH DB ?
    INPUT_STRING  DB 80 DUP('$')

    PROMPT_MSG         DB 'Enter a string (max 80 chars): $'
    PALINDROME_MSG     DB 0DH,0AH,'The string is a Palindrome.$'
    NOT_PALINDROME_MSG DB 0DH,0AH,'The string is NOT a Palindrome.$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, PROMPT_MSG
    MOV AH, 09H
    INT 21H

    LEA DX, MAX_LENGTH
    MOV AH, 0AH
    INT 21H

    MOV CL, ACTUAL_LENGTH
    MOV CH, 0

    LEA BX, INPUT_STRING
    ADD BX, CX
    MOV BYTE PTR [BX], '$'

    LEA SI, INPUT_STRING
    MOV DI, BX
    DEC DI   
    
CHECK_LOOP:
    CMP SI, DI
    JGE IS_PALINDROME

    MOV AL, [SI]
    MOV BL, [DI]

    CMP AL, BL
    JNE NOT_PALINDROME

    INC SI
    DEC DI
    JMP CHECK_LOOP

IS_PALINDROME:
    LEA DX, PALINDROME_MSG
    JMP DISPLAY_AND_EXIT

NOT_PALINDROME:
    LEA DX, NOT_PALINDROME_MSG

DISPLAY_AND_EXIT:
    MOV AH, 09H
    INT 21H

    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN