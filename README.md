# **this script is to get the subtraction of two hic matrix**
> **the input files should be of .cool format with a certain resolution**

## usage：

```
python hic_Subtraction.py file1.cool file2.cool -s 2000 -e 20000 -O outdir -fig outfig

Options:
    -s              default=0               comparasion start bin area
    -e              default=2000            comparasion end bin area
	  -O, --outdir    default="./"            path to output file.
    -fig, --outfig  default="test.png"      name of output figure
```

## example:
```
python hic_Subtraction.py example/6_10000.cool example/7_10000.cool -fig test.png

```
## example_result：
![avatar](example/test.png)
