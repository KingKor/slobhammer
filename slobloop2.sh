echo "Enter Loop Count [how often hammer will reset]: "
read count
while [ true ]; do
      sudo killall slobhammer.py
      sleep $count
done
