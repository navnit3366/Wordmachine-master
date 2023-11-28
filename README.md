# Wordmachine<br>
This is a program based on Python3.6 and released using Cx_freeze.<br>
To use it:<br>
## 1 Adding dictionaries:<br>
>Of course you can add your own dictionaries by putting your dictionary under the same directory of wordmachine.exe.<br>
>Notice!!! The dictionary should be UTF-8 without BOM. <br>
>The dictionary should be like this:<br>
```
  apple;苹果
  orange;橘子，橙子
```
>The meanings in Chinese can be seperated by anything but the  semicolon(;), for the program use it to seperate English and Chinese.
>This is because the program only search your input in the whole Chinese String, if the substring is founded then you input shall be
>considered correct. So if you want, you can even use nothing, though i won't recommend you to do that.<br>
  
## 2 About saving:<br>
>The program has a simple saving function, so don't panic if you close the program before you complete a list(or the program crash
>because of a bug). However this does not work in mistakes book mode.<br>
  
## 3 The mistakes book:<br>
>This program will add the word item into the file once you make a mistake, and it won't be reduplicated.<br>
>When you enter the mistakes book(MODE 4), your mistakes will be tested in EN-CN or CN-EN randomly, since you should have already
>completely mastered them<br><br>
  
So have fun then!
