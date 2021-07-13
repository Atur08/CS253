#!/bin/bash
touch Log
>Log

(

g++ -fprofile-arcs -ftest-coverage $1 -o cov1
gcno_file=$(ls -lt | sed -n 3p | awk '{print $9}')
PROGRAM_NAME=$(echo ${gcno_file/.gcno})

touch all_branches.txt
> all_branches.txt

rm *.gcda 

gcov -b -c $PROGRAM_NAME 

nl *cpp.gcov | grep branch > temp.txt
while IFS= read -r line; do 
	var=$(echo $line | awk '{print $1}')
       	echo -n $var " " >> all_branches.txt
done < temp.txt
echo >> all_branches.txt

rm temp.txt


touch branches.txt
> branches.txt

while IFS= read -r test; do
        echo $test | ./cov1;
        gcov -b -c $PROGRAM_NAME 
        nl *cpp.gcov | grep "taken 1" >> temp.txt

	while IFS= read -r test; do
		var=$(echo $test | awk '{print $1}') 
		echo -n $var " " >> branches.txt
		#echo -n " " >> branches.txt
        done < temp.txt
        echo >> branches.txt
        rm *.gcda temp.txt
done < $2

touch test/S
touch test/record.txt 
python3 script.py $2 $3

) >>Log

