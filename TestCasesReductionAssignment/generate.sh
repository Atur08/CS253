touch test/T
>test/T 
for (( i=0; i<$2; i++ ))
do	
	echo $((-1**$RANDOM*$RANDOM*$RANDOM*$RANDOM%$RANDOM)) $((-1**$RANDOM*$RANDOM*$RANDOM*$RANDOM%$RANDOM)) >> test/T
done
