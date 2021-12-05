#!/bin/bash -x

isPartTime=1
isfullTime=2
empRateHr=20
randomCheck=$((RANDOM%3))

case $randomCheck in
                $isPartTime)
			empHrs=4
                	;;
		 $isfullTime)
                        empHrs=4
                	;;
		*)
		empHrs=0
                	;;
esac
salary=$(($empHrs*$empRateHr))
