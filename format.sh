#!/usr/bin/env bash

# ./format.sh input.txt > output.txt
# ./format.sh input.txt output.txt

infile="$1"
outfile="${2:-/dev/stdout}"

awk '
{
    line=$0
    out=""
    in_math=0

    for (i=1; i<=length(line); i++) {
        c=substr(line,i,1)
        n=substr(line,i+1,1)

        # 遇到 $$ -> 直接输出并跳过
        if (c=="$" && n=="$") {
            out=out "$$"
            i++
            continue
        }

        # 遇到单 $
        if (c=="$") {
            if (in_math==0) {
                # 左侧如果不是空格，补空格
                if (length(out)>0 && substr(out,length(out),1)!=" ")
                    out=out " "
                out=out "$"
                in_math=1
            } else {
                out=out "$"
                # 右侧如果不是空格且不是行尾，补空格
                nextc=substr(line,i+1,1)
                if (nextc!="" && nextc!=" ")
                    out=out " "
                in_math=0
            }
            continue
        }

        out=out c
    }

    print out
}
' "$infile" > "$outfile"