#!/bin/bash
touch $3
>$3

(g++ -fprofile-arcs -ftest-coverage $1 -o cov1
gcno_file=$(ls -lt | sed -n 3p | awk '{print $9}')
PROGRAM_NAME=$(echo ${gcno_file/.gcno})


while IFS= read -r test; do
        echo $test | ./cov1;
        gcov -b -c $PROGRAM_NAME 
done < $2) >>$3

cat $3 | grep Taken > temp.txt
cat temp.txt > $3
rm temp.txt 
