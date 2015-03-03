#!/bin/bash

wget -r -nH --no-parent --reject="index.html*","*mar*","*debug*" https://dist.torproject.org/torbrowser/
cd tbb-bin
git add -A
for file in `git status | egrep 'modified|new file' | awk -F: '{print $2}'`; do
  git commit -o $file -m "$file";
  git push
done
curl -d '{"title":"Update","head":"USER:master","base":"master"}' https://api.github.com/repos/glamrock/tbb-bin/pulls -u USER:PASS
