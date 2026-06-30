; dvd logo
; by las-r

; constant registers
LDI R1 1
LDI Re 2

; setup values
LDI R2 1  ; dx
LDI R3 1  ; dy
LDI R4 60 ; x (Kept safe!)
LDI R5 30 ; y

; set i to sprite
LDI Rb dvd_sprite
STI Rb

; boundary constants
LDI R6 0
LDI R7 120
LDI R8 61

; timer delay
LDI R9 2

; loop start
LDI Ra main_loop
main_loop:
    CLR
    DRW R4 R5 3

    ; move x
    ADD R4 R4 R2
    SKE R4 R7
    JPR Re
    LDI R2 0xFF ; hit right wall
    SKE R4 R6
    JPR Re
    LDI R2 1 ; hit left wall

    ; move y
    ADD R5 R5 R3
    SKE R5 R8
    JPR Re
    LDI R3 0xFF ; hit bottom wall
    SKE R5 R6
    JPR Re
    LDI R3 1 ; hit top wall

    ; timer
    STT R9
    WTT
JMP R0 Ra R0

; sprite data
dvd_sprite:
    RAW 0x7ee7
    RAW 0x7e00
