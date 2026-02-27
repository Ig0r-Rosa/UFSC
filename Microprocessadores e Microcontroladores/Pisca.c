/*
 * File:   main.c
 * Author: igord
 *
 * Created on 1 de Fevereiro de 2022, 15:22
 */
#include <xc.h> //include padrão
#include <stdio.h> //padrão do C
#include <pic16f877a.h>//

#define _XTAL_FREQ 4000000 //frequencia do cristal

void Delay()
{
  __delay_ms(1000);  
};

void AcendeLED()
{
    PORTCbits.RC3 = 1;
    PORTCbits.RC7 = 0;
    Delay();
};

void ApagaLED()
{
    PORTCbits.RC3 = 0;
    PORTCbits.RC7 = 1;
    Delay();
};

void main(void) {
    
    TRISC = 0;
    
    while(7)
    {
        AcendeLED();
        ApagaLED();
    }
}
