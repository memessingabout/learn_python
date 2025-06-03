#!/bin/bash

for i in {1..30}
do
  filename="day_${i}.py"
  echo '""" Today we will learn ... """' > "$filename"
  echo "$filename created."
done
echo "All files created successfully."