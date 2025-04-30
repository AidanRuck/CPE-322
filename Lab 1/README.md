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
