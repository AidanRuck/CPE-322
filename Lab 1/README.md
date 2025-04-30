# Lab 1 - GHDL and GTKWave
### *"I pledge my honor that I have abided by the Stevens Honor System" -Aidan Ruck*

## Half-Adder Example
```
$ ghdl -a ha.vhdl
$ ghdl -a ha_tb.vhdl
$ ghdl -e ha_tb
$ ghdl -r ha_tb --vcd=ha.vcd
ha_tb.vhdl:47:5:@5ns:(assertion error): Reached end of test
$ gtkwave ha.vcd
```
![image](https://github.com/user-attachments/assets/e9af63c0-4796-4945-b452-2f0ab9e0598d)

## D Flip-Flop Example
```
$ ghdl -a dff.vhdl
$ ghdl -a dff_tb.vhdl
$ ghdl -e dff_tb
$ ghdl -r dff_tb --vcd=dff.vcd
$ gtkwave dff.vcd
```
![image](https://github.com/user-attachments/assets/9c887d65-0590-4100-a90c-d6e5341a8e05)
