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
> origin figure  from bin 0 to 2000
> file1
![avatar](example/6.orign.png)
>file2
![avatar](example/7.orign.png)

> file1-file2 substraction result from bin 0 to 2000 with different color style
> with blue plots means file1's intensity is lower than file2, and hot color ones means in contrast
![avatar](example/test.png)
![avatar](example/test1.png)
