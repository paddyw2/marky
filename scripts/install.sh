#!/usr/bin/env bash
 
echo 'Installing marky...'
cd
git clone https://github.com/paddyw2/marky.git
mv marky .marky
cd .marky/scripts
chmod +x marky
cp marky /usr/local/bin
echo 'Finished'
echo "Type 'marky' to get started"
