sudo chmod -R 755 slob.sh slob2.sh slob3.sh slobloop.sh
cd ~
echo 'alias tor1="/usr/sbin/tor -f ~/sexploits/slobhammer/torrc2"' >> .bash_aliases
echo 'alias tor2="/usr/sbin/tor -f ~/sexploits/slobhammer/torrc3"' >> .bash_aliases
source ~/.bash_aliases
