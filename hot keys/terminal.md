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

