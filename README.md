# Bowienator
A command line application that uses face detection to slap a picture of David Bowie's face over faces in the picture.


### Sample Command

Let's say that you have a picture of popular Swedish pop group ABBA:

![ABBA before](/gallery/ABBA/ABBA_Before.jpg?raw=True)

And instead of Agnetha, Björn, Anni-Frid, and Benny; you want to see 
Aladdin Sane era David Bowie. You can enter a command line at the directory
holding the bowienator.py script, and enter

```
> bowienator.py path/to/the/image/file/here.whatever
```

The script will run, and automatically detect faces in the photo, put the David Bowie
picture over theirs, and save the picture in the same directory as the original.

If you ran that picture of ABBA through the program, you would get:

![ABBA After](/gallery/ABBA/ABBA_After.png?raw=True)

And that's how it done.

### Thanks

..* Thanks to the teams behind OpenCV and Pillow - this entirely frivolous project would not exist without you.

..* Thanks to my family and friends for all the support they give me in everything I do.

..* Special thanks to Jabari King, who got me into programming and has always helped me when I had a problem.

..* Of course, thanks to David Bowie, for making such rad music.

..* Thanks for you, for showing interest in an amateur programmer's projects! It means a lot.
