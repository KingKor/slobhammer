echo "Enter Loop Count [how often hammer will reset]: "
read count
while [ true ]; do
      sudo killall slobhammer.py
      sleep $count
      sudo killall slobhammer2.py
      sleep $count
      sudo killall slobhammer3.py
      sleep $count
done
