# H-brido-Cl-ssico-Qu-ntico
Programa Clássico 

### Documentação Completa do Programa Híbrido Clássico e Quântico

**Título:** Programa Híbrido de Computação Clássica e Quântica Simulada dos Anos 1950-60

**Versão:** 1.0

**Data:** 28 de Dezembro de 2024

**Autor:** Adilson Oliveira

---

#### **Objetivo do Programa**

Este programa visa demonstrar a integração de técnicas de programação clássica com um conceito simplificado de computação quântica, adaptado ao contexto tecnológico dos anos 1950-60. O programa calcula a soma de uma série numérica de 1 a 10 e realiza uma simulação de um estado binário aleatório que emula o comportamento de um qubit em um sistema clássico.

---

#### **Componentes e Métodos**

1. **Soma de Série Numérica:**
   - Utiliza-se a fórmula de soma dos primeiros $n$ números naturais:
     $$
     \text{Sum} = \frac{n(n+1)}{2}
     $$
     Para $n = 10$:
     $$
     \text{Sum} = \frac{10(10+1)}{2} = \frac{10 \times 11}{2} = 55
     $$

2. **Simulação de Qubit:**
   - Em vez de verdadeiros qubits, utilizamos um gerador de números aleatórios para simular um estado binário (0 ou 1) com probabilidade igual, que é uma abstração simples do conceito de superposição e colapso de estado quântico.

---

#### **Implementação**

##### **Assembly (Simulação de CPU da Era)**
```assembly
; Soma de uma série numérica
START:  LDA #0            ; Carrega 0 no acumulador
        STA SUM           ; Armazena 0 em SUM
        LDA #10           ; Carrega 10 no acumulador (n)
        STA COUNT         ; Armazena 10 em COUNT
LOOP:   LDA SUM           ; Carrega SUM no acumulador
        ADD COUNT         ; Adiciona COUNT ao acumulador (SUM += COUNT)
        STA SUM           ; Armazena o novo valor em SUM
        DEC COUNT         ; Decrementa COUNT
        BNE LOOP          ; Se COUNT não for zero, volta ao LOOP
        JSR PRINT_SUM     ; Chama a rotina para imprimir a soma
        JSR PRINT_QUBIT   ; Chama a rotina para simulação de qubit
        HLT               ; Parar o programa

PRINT_SUM:
        ; Implementação para impressão de SUM
        ; Cálculo matemático: SUM = 1 + 2 + 3 + ... + 10 = 55
        RTS

PRINT_QUBIT:
        LDA #$01          ; Carrega um valor aleatório (emulação)
        AND RANDOM_REG    ; AND com um registrador de valor aleatório (0 ou 1)
        BNE QUBIT_ONE      ; Se resultado não é zero, vai para estado 1
        LDA #$00          ; Se zero, carrega 0
        JMP PRINT_STATE
QUBIT_ONE:
        LDA #$01          ; Carrega 1
PRINT_STATE:
        ; Implementação para impressão do estado binário
        RTS
```

##### **Fortran (Foco em Cálculos Matemáticos)**
```fortran
PROGRAM SERIES_SUM_ADILSON_OLIVEIRA
  INTEGER :: N, SUM, RANDOM_STATE
  SUM = 0
  DO N = 1, 10
    SUM = SUM + N  ! Acumulando cada número de 1 a 10
  END DO
  PRINT *, "Soma da série é:", SUM  ! SUM = 55
  
  ! Simulação de comportamento probabilístico
  CALL RANDOM_NUMBER(R)
  RANDOM_STATE = INT(R * 2)  ! 0 ou 1 como se fosse um qubit, probabilidade 50%
  PRINT *, "Estado aleatório (como um qubit):", RANDOM_STATE
  
  ! Verificação matemática da soma
  IF (SUM == (10*11)/2) THEN
    PRINT *, "Verificação da soma: Correta"
  ELSE
    PRINT *, "Verificação da soma: Incorreta"
  ENDIF
END PROGRAM
```

##### **COBOL (Foco em Relatórios e Legibilidade)**
```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SERIES-REPORT-ADILSON-OLIVEIRA.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 SUM PIC 9(03) VALUE 0.
01 COUNT PIC 9(02) VALUE 10.
01 RANDOM-STATE PIC 9 VALUE 0.
01 VERIFICATION PIC X(10) VALUE 'Incorreta'.
PROCEDURE DIVISION.
    PERFORM VARYING N FROM 1 BY 1 UNTIL N > COUNT
        ADD N TO SUM  ! Soma acumulativa
    END-PERFORM
    DISPLAY "SOMA DA SÉRIE: " SUM  ! SUM = 55
    
    COMPUTE RANDOM-STATE = FUNCTION RANDOM * 2  ! Estado binário aleatório
    DISPLAY "ESTADO ALEATÓRIO (como um qubit): " RANDOM-STATE
    
    IF SUM = (COUNT * (COUNT + 1)) / 2 THEN
       MOVE 'Correta' TO VERIFICATION  ! Verificação matemática
    END-IF
    DISPLAY "VERIFICAÇÃO DA SOMA: " VERIFICATION
    STOP RUN.
```

##### **LISP (Recursão e Listas)**
```lisp
; Soma de uma série numérica por Adilson Oliveira
(defun sum-series-adilson-oliveira (n)
  (if (= n 0)
      0
      (+ n (sum-series-adilson-oliveira (- n 1)))))  ; Recursão para somar de n até 0

; Simulação de um estado binário aleatório
(defun simulate-qubit-like-adilson-oliveira ()
  (if (< (random 1.0) 0.5)
      0
      1))

; Verificação matemática
(defun verify-sum-adilson-oliveira (n sum)
  (= sum (/ (* n (+ n 1)) 2)))  ; Verificação usando a fórmula da soma

(let* ((result (sum-series-adilson-oliveira 10))
       (qubit-state (simulate-qubit-like-adilson-oliveira)))
  (format t "Soma da série: ~A~%" result)  ; result = 55
  (format t "Estado aleatório (como um qubit): ~A~%" qubit-state)
  (format t "Verificação da soma: ~A~%" 
    (if (verify-sum-adilson-oliveira 10 result) "Correta" "Incorreta")))
```

##### **ALGOL (Estrutura Clara e Precisão Científica)**
```algol
begin
  integer i, sum, state;
  sum := 0;
  for i := 1 step 1 until 10 do
    sum := sum + i;  ! Acumulando cada número de 1 a 10
  print("Soma da série: ", sum);  ! sum = 55
  
  ! Simulação de um estado binário aleatório
  state := entier(random(2));  ! 0 ou 1, probabilidade 50%
  print("Estado aleatório (como um qubit): ", state);

  ! Verificação matemática
  if sum = (10 * 11) / 2 then begin
    print("Verificação da soma: Correta");
  end else begin
    print("Verificação da soma: Incorreta");
  end
end;
```

---

#### **Resultados Esperados**

- **Soma da Série:** 55 (verificado pela fórmula matemática)
- **Estado Aleatório (Qubit Simulado):** 0 ou 1, com probabilidade de 50% para cada.

Este programa, criado por Adilson Oliveira, fornece uma visão sobre como poderíamos imaginar a integração de conceitos de computação clássica com a simulação de comportamentos quânticos dentro das limitações tecnológicas da época.
