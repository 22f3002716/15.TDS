# for f in *; do 
#     mv "$f" "$(echo "$f" | sed 'y/0123456789/1234567890/')"
# done
#!/bin/bash
for f in *; do
    # Skip directories and the script itself
    [ -f "$f" ] || continue
    [ "$f" = "command.sh" ] && continue

    newname=$(echo "$f" | sed 'y/0123456789/1234567890/')
    mv "$f" "$newname"
done