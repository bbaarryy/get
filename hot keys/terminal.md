### Weather

```curl wttr.in/Sochi```

### Battery

```sudo tlp start```

https://www.altlinux.org/TLP#Работа_в_терминале

```sudo tlp stat -b```

### Print queue

```lpq```


### Move - delete - links
```mkdir dir1 dir2``` - создание директории

```cp item1 item2```  - копирование item1 в item2:
- -i - запрашивать разрешение у пользователя
- -v - вывод действий 
- -u - перезапивать только новые файлы

```mv``` - перемещение, аналогично

```rm``` - удаление
- -i - questions
- -r - recursive
- -f - force
!!!Warning!!! 

```ln``` - создание ссылок

```ln file link``` - hard-link

```ln -s file link``` - symb-link

```file``` - узнать что это за файл

```$()``` -  передача переменной

```su [[-l]] [user]``` - запуск командной строки от имени другого пользователя
```-l ``` - всю ли командную оболочку перестроить?

### Procceses

```fg %1``` - front, вернуть на передний план
```bg %1``` - background, на задний план

```kill -[signal] PID```

2 - INT Прервать

9 - KILL Уничтожить

15 - TERM Завершить

18 - CONT Продолжить 

19 - STOP Продолжить

```ps``` - вывод всех процессов
```jobs``` - вывод всех работ?

```pstree``` - вывод всех процессов в древовидной структуре

```tload``` - график загруженности процессора в терминале

Файл с конфигурациями командной оболочки:
```~/.bashrc```

crontab хранится в папке ```/etc/cron.d/```

```find / -type -f/-d/-l(symbol link) -name "*.JPG" -size +1M ```

cancel -a

### VIM

:q - quit

:w - save changes

x - delete

3x - delete 3 symbols

dd - delete current string

yy - copy current string

p - paste from clipboard

i - insert mode

esc - escape insert mode

J - join strings

fa - find symbol a in current string

; - repeat command

/find_word - find word

n - repeat find word

:%s/строка/Строка/gc - совершить подстановку с заменой
 ^^- тип подстановки
все строки

:r file.txt - paste file.txt

```neofetch``` - rhose cool command

```echo $XDG_SESSION_TYPE``` - x11 or wayland

```sudo tail -f /var/log/syslog``` - вывод происходящего

```xmodmap -e "keycode 133 = Super_L"```
```xmodmap -e "keycode 64 = Alt_L"```


### FIND

```plocate имя_файла```

```find директория имя_файла```

-type d\f

-name "*.JPG"

-iname == name + Registor

-size +1M

Operators:

```find ~ \( -type f -not -perm 0600 \) -or \( -type d -not –perm 0700 \)```

Также можно добваить исполняемые действия в конец find: -delete -print

Свои действия в конце:

-find .... -ok echo "hello" '{}' ';' с подтверждением

-find .... -exec echo "hello" '{}' ';' без подтверждения

для увеличения продуктивности можно объединить команды , заменив ';' на +

ИЛИ при помощи XARGS

find ~ -type f -name 'foo*' -exec ls -l '{}' +
equal
find ~ -type f -name 'foo*' -print | xargs ls -l

Для пробельных имен:

find ~ -iname '*.jpg' -print0 | xargs --null ls -l

find playground \( -type f -not -perm 0600 -exec chmod 0600 '{}' ';' \) -or \( -type d -not -perm 0700 -exec chmod 0700 '{}' ';' \)

find директория -regex ~RE~

### Archive

gzip file - сжатие
gunzip file - разжатие

bzip\bunzip - analog

tar cf playground.tar playground - compress directory with name playground
режимы

c Создать архив из списка файлов и/или каталогов
x Извлечь файлы из архива
r Добавить указанный файл и/или каталог в конец архива
t Вывести список содержимого архива

rsync параметры источник приемник
rsync -av playground foo
sudo rsync -av --delete /etc /home /usr/local /media/BigDisk/
backup

### Regular Expressions - standart POSIX

. - any symbol

ankors: ^ - beginof string, $ - end of string

[123456] - any from this list

[^123456] - deny of list

[1-9a-z] - diapozone

Extended RE

| - or

? - privious 0 or 1

* - privious >=0 times

+ - privious >=1 times

{n} - privious n times

### Another text?

sort 
-n - numeric sort
-f - force(without registre)
-r - recoursive
-b - ignore-leading-blanks(recomended)
-k - key:
    -t - castom separator
    -k 5(number of field)n...
    -k 6.1(6 field, 1 symbol)

cut
    -d - castom separator
    -f(field) ~number~ 
    -c(characters) ~diapozone~

diff
    -c - contest compare
    -u - unificated format
    Pathching diff. versions
        diff -Naur ~oldfile~ ~newfile~ > patchfile.txt
        patch < patchfile.txt 

tr - replace symbols
    cat -A foo.txt | tr ',' ':' > foo1.txt
    tr -d - delete symbols

sed - intro
    sed -n(подавление вывода по умолчанию) '~address~ ~command~' ~input_file~

