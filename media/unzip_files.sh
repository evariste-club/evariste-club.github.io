#!/bin/bash

for i in $(ls *.zip)
do
	unzip $i -d ${i:0: -4}
done
