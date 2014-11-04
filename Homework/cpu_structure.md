#CPU Structure Homework

You should refer to the **homework policy** for details on how this homework should be submitted.

**Attempt all questions and show all working.**

##Question 1
Some of the components of a computer system are:

- processor
- main memory
- address bus
- data bus
- control bus
- I/O port
- secondary storage

![](https://www.dropbox.com/s/iz0wz7kr1ltjt6o/cpu_diagram.jpg?dl=1)

The diagram above shows how these components are connected.

1. Using the list of components above name each of the following:

    1. *main memory*
    2. *Processor*
    3. *I/O port*
    4. *Address Bus *
    5. *Control Bus*

    (**5 marks**)

##Question 2
What is the function of the following components:

1. **processor**:  
*The CPU of a computer is a piece of hardware that carries out the instructions of a computer program. It performs the basic arithmetical, logical, and input/output operations of a computer system. *
2. **main memory**: 
*Main memory is for storing data so the CPU and other direct memory access devices can call up to fetch or store data for processing. *
3. **secondary storage**:
*The function of secondary storage is the long-term memory of data in a computer system.*

(**3 marks**)

##Question 3
Give **two** examples of a signal carried by the control bus.

1. *Actual data being processed*
2. *commands from the CPU*

(**2 marks**)

##Question 4
Apart from data, what else is carried on the data bus?

*It returns status signals from the device*

(**1 mark**)

##Question 5
A single accumulator microprocessor supports the assembly language instructions:

```
LOAD memory reference
ADD memory reference
STORE memory reference
```

An example instruction is:

```
LOAD 4
```

This instruction would copy the contents of the referenced memory location **4** into the accumulator register.

1. Identify which part of the instruction is the __*operand*__ and which part is the __*opcode*__ by writing the words in the two table below.

    |LOAD|4|
    |----|-|
    |op-code|operand(s)|

    (**1 mark**)

2. The accumulator is a general purpose register. Define the term register? (**1 mark**)
*It is allocated on the processor, for fast retrievals.*
3. Using the given assembly language instructions, write an assembly language program that adds together the values stored in memory locations 12 and 13, storing the resulting total in memory location 14. 

|op-code|operand(s)|
|-|-|
|ADD|12|
|ADD|13|
|STORE|14|


(**3 marks**)

##Question 6
The diagram below shows the fetch-execute cycle. Some of the steps have been described.

![](https://www.dropbox.com/s/xzt95i7xa8hghef/fe_cycle.jpg?dl=1)

Describe the missing steps, using either register transfer notation of a written description. Steps 2 and 3 occur at the same time.

1. *Copy content of PC to M *
2. `PC ← [PC] + 1` or *increment contents of program counter register*
3. *answer here*
4. `CIR ← [MBR]` or *transfer contents of memory buffer register to current instruction register*
5. *answer here*
6. `[CIR] decode and execute` or *execute instruction in current instruction register*

(**3 marks**)

##Question 7
What would the effect on the performance of the computer system of increasing the

1. width of the data bus?*Data Bus The number of wires in a data bus determines the quantity of data that the bus can carry at any one time*
2. width of the address bus? *
3. clock speed? *The amount of ticks per second* 

(**3 marks**)

**Total 22 marks**


