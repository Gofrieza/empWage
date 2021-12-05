#!/bin/bash -x

partTime=1
absent=0
fullTime=2
empRateHr=40
randomCheck=$((RANDOM%3))

if [ $fullTime -eq $randomCheck ]
then
	empHrs=8;
	salary=$(($empHrs*$empRateHr));

elif [ $partTime -eq $randomCheck ]
then
        empHrs=4;
	salary=$(($empHrs*$empRateHr));
else
        empHrs=0;
fi
