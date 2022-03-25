#!/usr/local/bin/bash

export FILE=Level-2/min_unique_array_sum.py

git filter-repo --invert-paths --path $FILE --force
echo $FILE >> .gitignore
git push origin --force --all
git push origin --force --tags
