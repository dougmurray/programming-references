# Some good vim commands recently learned

The source of all this is from YouTube, who knew! This list is mainly from **The Primeagen**, *Vim As Your Editor- Horizontal* video. Plus his other Vim course videos.

Remember **CTRL c** is the same as Esc!

## Command Count Motion

### Commands

- d delete
- c change
- y copy
- v visual mode
- A insert at end of line
- I insert at begining of line
- ciw change word that cursor is on
    - if you use w and b this isn't usually necessary
- o insert line below cursor, insert mode
- O insert line above cursor, insert mode
- / search
    - n for next item
- * to search for word cursor is on
- vi( to select all text inside () and insert mode
- viw **God command**, select whole word cursor is on
- *iw* type commands are the most used
    - think yiw or yiW
----
- VY for visual yank to end of line
- YD for visual delete to end of line
    - preferred over yy or dd
----
- ya( yanks all text between (and including) )
    - think alternative vi(y

### Motion

- w move one word forward
- b move one word backward
- _ like 0, move to front of line
- $ move to end of line
- f find to right of cursor on line
    - f( move to first (, then can do *a* for insert **after**
        - can use f with any other character to find on line
        - can use ; to go to *next* ( on same line
        - can use , to go *back* to previous ( on same line
    - F( is move to previous (
        - can use F with any other characters to find on line
        - think combining with commands like 
- >> or << to indent right or left, DTM favorite
    - can indent whole sections: V>
- CTRL d and CTRL u for page down and page up

bob totally(dude) but not (absolute dude):

## Vim as a system

After `vim .` command. Or you can also just be in Vim and do :Explore (:Ex TAB).

- % make new file
- d make new directory (folder)
- CTRL w CTRL v copy buffer, side by side view
    - CTRL w w to switch between buffers
- D delete file or directory, **BE CAREFUL**

