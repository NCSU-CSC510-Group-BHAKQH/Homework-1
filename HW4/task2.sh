grep -l "sample" dataset1/* | xargs grep -o "CSC510" | uniq -c | awk '$1 >= 3 {print $1" "$2}' | sort -nr | gawk -F '[: ]' '{sub("file_", "filtered_", $2); print $2}'
