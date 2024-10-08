#!/bin/bash

awk -F, '$3 == 2 && index($13, "S") > 0 { gsub(/(^|,)male(,|$)/, ",M,", $0); gsub(/(^|,)female(,|$)/, ",F,", $0); if ($7 != "") { total_age += $7; count++; } print $0 } END { if (count > 0) { print "Average Age:", total_age / count } else { print "No passengers found." } }' OFS=',' titanic.csv
