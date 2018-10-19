#!/bin/bash
#Downloads the answer given the link for the quora.
TMP_FILE=${HOME}/tmp/q.html
wget $1 -O ${TMP_FILE}
tidy -mi -html -wrap 0 -q ${TMP_FILE}
grep -f ~/linuxcommands/scripts/q.txt ${TMP_FILE} | sed -e 's/<[^>]*>//g' | sed -e 's/&#\d*//g' > ~/tmp/a
less ~/tmp/a


