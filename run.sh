#!/bin/bash


for day in {1..25}
do
  echo "Running day $day ..."
  cd day$day
  time ./day$day.py
  echo
  cd ..
done
