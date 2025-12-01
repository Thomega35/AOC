#!/bin/bash
for day in {1..25}
do
   for part in 1 2
   do
      mkdir -p "j${day}/part_${part}"
      cp "template.py" "j${day}/part_${part}/solution.py"
      cp "utils.py" "j${day}/part_${part}/utils.py"
      touch "j${day}/part_${part}/input.txt"
   done
done
