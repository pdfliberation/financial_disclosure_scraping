pagenum=0

DIR=$1

for fn in $(find $DIR -iname '*.pdf')
    do 
        num=`pdfinfo $fn | grep Pages | grep -o [0-9]*`
        if (($num))
        then 
            ((histogram[${num}]++));
            pagenum=$(( $pagenum + $num))
        fi; 
    done; 

echo "${pagenum} total pages"
echo "======================"
printf "%-15s %s\n" "page_count" "number_of_files"
for count in "${!histogram[@]}"
do
    printf "%-15s %s\n" "${count}" "${histogram[$count]}"
done

echo "\n\n"
