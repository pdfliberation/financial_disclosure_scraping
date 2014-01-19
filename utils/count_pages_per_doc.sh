DIR=$1

for fn in $(find $DIR -iname '*.pdf')
    do 
        num=`pdfinfo $fn | grep Pages | grep -o [0-9]*`
        if (($num)); 
        then 
            echo -e "${fn}\t$num"
        fi; 
    done; 
echo $pagenum

