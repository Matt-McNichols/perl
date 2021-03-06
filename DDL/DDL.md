
===
DDL
===

---
Week 1:
* lecture 8/24/15:
  *  Website: http://ecee.colorado.edu/~ecen3000/
  *  ![Lecture 1](https://github.com/Matt-McNichols/perl/blob/master/DDL/class_8_24_15.jpg)
  *  Lab 1 due Tuesday 9/1/15

---
Week 2:

* Lecture 8/31/15:
  * Lab 1 due tomorrow
  * prelab 2 due tomorrow
  * include header files
  * two libs
    * make sure the paths are known
      * gcc (path, name) FIXME
    * cmsis(ARM)
    * lspcxpresso
  * cortex M0:
    * Firmware: software that controls the hardware
      * very specific
    * registers:
      * 16 - instructions (only uses low registers)
      * 32 - instructions (uses all registers)
      * registers run at the same speed as microprocessor
      * R0-R7  lower regs
      * R8-R16 higher regs
      * special regs: SP,LR,PC
      * flag regs:  NZVC
    * Calling conventions:
      * R15: PC
      * R14: LR
      * R13: SP
      * R0-R3: subroutine arguements
        * for more than 4 arguments use a pointer
      * R4-R11: local variables
      * R12:  Intra-Procedure scratch reg (not important)
      * when variable is pushed on the stack SP is incremented by 1
    * Lab 2: write fib. seq. (write using recursion in assembly)
      * why?  lots of program calls. you will need to handle stack properly
    * Lab 3: write using interrupts
    * Interrupts:
      * signal that indicates to the processor there is an event that needs immediate attention.
      * systick: 15  system timer
      * IRQ0-IRQ31: 16-47
      * Interrupt generator:
        * read out the frequency of ADC
        * ADC detects the rising edge
          * interrupt on rising edge
          * run frequency application
            * change PC to ISR
            * memory:
              * interrupt #0 at address 0x40
              * value at address 0x40 is a pointer to ISR#0
              * PC=(#intr*4 + 0x40)
            * check the system clock every time interrupt occurs
            * freq= 1/(Cnew-Cold) 
 
<body> 
<ul>
  <li><a href="http://ecee.colorado.edu/~ecen3000/lecture/l4.pdf">lecture 9/14/15: Power Lab</a></li>
  <ul>
  <li>Lab three is an interrupt</li>
  <li>2004--AMD make multicore microprocessor</li>
  <li>took intel two years to catch up</li>
  <li>power grows exponentially with performance</li>
  <li>power density (W/cm^2)</li>
  <li>cfv^2</li>
  <li>Dell's Law:  cooling and packaging cost after >40W: 1$->1W </li>
    <ul>
    <li>1 to 1 relationship between power and cooling</li>
    <li>now down to 1W of power -> 180 mW</li>
    <li>The big issue is battery life</li>
    <li>Battery storage has not improved much</li>
    <li>Screen waisting power. E-ink screen doesnt consume power to display (Kindle)</li>
    <li>CMOS transistor used as an inverter</li>
    <li>capacitor does not consume power the transistors are not a perfect switch</li>
    </ul>
  <li>use different modes of operation: "run","sleep", ect</li>
  <li>use interrupts to allow microprocessor to rest while not needed</li>
  <li>ARM insterrupt inst:  __WFE[], __WFI, use sleep on exit feature</li>
  <li>PMU(power management unit) off chip unit has ability to store crucial data</li>
  <li>PCON: Controls deep sleep vs soft sleep</li>
  </ul>
<li>Problem:  Lose control of the bord: when you put M0 into deep sleep, they disable the JTAG port</li>
  <ul>
  <li> There is a way to reset the bord</li>
  <li> 2 firmwares: your code and bootloader (Read the couple PP) </li>
  </ul>
<li> common mistake: how to measure the power consumption. put 1 ohm R between cpu and board because we cannot measure the current directly.  know input voltage so, p=v^2/R but that is the power accross the resistor. Do v/r and get a current, p=(Vdd-Vr)I</li>
</ul>
</body>
