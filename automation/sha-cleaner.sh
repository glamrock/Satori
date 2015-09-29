#!/bin/bash

## sha256 cleaner for tor-bin/sha-temp.txt
# 
# Author: Griffin Boyce, griffin@cryptolab.net
# converts sha256sum files into json entries for Satori
# be sure to name your file sha-temp.txt before running


# delete debug and incremental entries
sed -i '/.mar/d' ./sha-temp.txt
sed -i '/debug./d' ./sha-temp.txt

# remove initial 2 spaces
sed -i 's/^  //g' ./sha-temp.txt 

# delete duplicate (sequential) lines
sed -i '$!N; /^\(.*\)\n\1$/!P; D' sha-temp.txt

# add the beginning
sed -i 's/^/{"sha256sum":"/' ./sha-temp.txt

# the necessary middle
sed -i 's/  /", "title":"/g' ./sha-temp.txt 

# append the end of the line
sed -i 's/$/"},/g' ./sha-temp.txt 


# delete any empties
sed -i 's/{"sha256sum":""},//g' ./sha-temp.txt
sed -i 's/^", "title":"{"/{"/' ./sha-temp.txt # fix common duplication error


# clean up Tor software titles
sed -i 's/TorBrowser-/Tor Browser for Mac v/g' ./sha-temp.txt 
sed -i 's/tor-browser-/Tor Browser for Linux v/g' ./sha-temp.txt 
sed -i 's/torbrowser-install-/Tor Browser for Windows v/g' ./sha-temp.txt 
sed -i 's/linux64-//g' ./sha-temp.txt
sed -i 's/linux32-//g' ./sha-temp.txt
sed -i 's/-osx64//g' ./sha-temp.txt

# remove extensions
sed -i 's/.dmg//g' ./sha-temp.txt 
sed -i 's/.exe//g' ./sha-temp.txt 
sed -i 's/.tar.xz//g' ./sha-temp.txt 

# fix language declaration
sed -i 's/_ar/ (ar)/g' ./sha-temp.txt 
sed -i 's/_de/ (de)/g' ./sha-temp.txt 
sed -i 's/_en-US/ (en-US)/g' ./sha-temp.txt 
sed -i 's/_es-ES/ (es)/g' ./sha-temp.txt 
sed -i 's/_fa/ (fa)/g' ./sha-temp.txt 
sed -i 's/_fr/ (fr)/g' ./sha-temp.txt 
sed -i 's/_it/ (it)/g' ./sha-temp.txt 
sed -i 's/_ko/ (ko)/g' ./sha-temp.txt 
sed -i 's/_nl/ (nl)/g' ./sha-temp.txt 
sed -i 's/_pl/ (pl)/g' ./sha-temp.txt 
sed -i 's/_pt-PT/ (pt-PT)/g' ./sha-temp.txt 
sed -i 's/_ru/ (ru)/g' ./sha-temp.txt 
sed -i 's/_tr/ (tr)/g' ./sha-temp.txt 
sed -i 's/_vi/ (vi)/g' ./sha-temp.txt 
sed -i 's/_zh-CN/ (zh-CN)/g' ./sha-temp.txt 

