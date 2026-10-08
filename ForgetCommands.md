##Decode-encode files:

#check encoding:
    # may cause errors
    file -i <yourfile>.txt

    # more correct
    enca -L ru <yourfile>.txt
#decode:
    iconv -f CP1251 -t UTF-8 <currentFile>.txt > <new_file>.txt


##Split .flac file with .cue file
    shnsplit -f file.cue -t %n-%t -o flac file.flac


