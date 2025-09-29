# Vim Commands
These commands were derived by the vimtutor, however some were just found randomly or by online searching.

## Tried and Trues:

Remember **CTRL c** is the same as Esc!

- :Ex <tab> explores file system
- :new splits the current window, adding an empty window, best approach*
- CTRL w CTRL w or CTRL w w switches between windows
- line number G to move to line number in file
- w move to next word (to beginning of word)
- b move to begining of word ("backwards" move)
- _ like 0, move to front of line
- $ move to end of line
- A append at end of line
- I insert at begining of line
- f find char on line
    - great for combos like *vf char*, DTM favorite
    - use ; and , for find next, forward and backwards
- t find char on line, cursos ends up *right before* found char
    - great for combos like *ct char*, DTM favorite
- viw **God command**, select whole word cursor is on, DTM favorite
    - *iw* type commands are the most used
        - ciw or viw or yiw or diw
        - ciw change word that cursor is on
- vi( to select all text inside () and insert mode
    - Can also do ci( for between (), *works for empty () too*
- o insert line below cursor, insert mode
- O insert line above cursor, insert mode
- * will search all words like one under cursor
    - / searches
        - n for next item
- CTRL v then arrows, followed by SHIFT i or SHIFT a to column select and
- CTRL N is for autocomplete a word
- >> or << to indent right or left, DTM favorite
    - can indent whole sections: V>
- CTRL d and CTRL u for page down and page up
- :%s/old/new/gc to substitute all old words with new worlds in file, one-at-time
- Macros: qq starts macro, do some commands then, q to stop macro. Finally @q to repeat macro
    - the second q in qq and in @q is the register designator, it could be anything
        - the macro format is: q<register><commands>q
    - to view the macros, checkout the registers with :reg, or :regq for the specific one
    - try to start you macro with 0 to set the beginning point at same point
- :terminal starts a terminal, switch with CTRL w w and close with CTRL w c

## Lessons:

Lesson One:
- u is undo!!!
- U to undo all edits in line
- CTRL r to redo
- x delete character
- dw delete word
- A append at end of line
- d$ delete from cursor to end of line
- w move to next word (to beginning of word)
- e move to end of word (to end of word, think de)
- b move to begining of word ("backwards" move)
- $ move to end of line
- 0 move to start of line
- } move forward by paragragh (the next blank line)
- dd delete whole line (can do anywhere in line)
- p paste (nice for moving whole lines, dd then p)
- r replace, followed by charater to replace
- ce delete from cursor to end of word (you go into Insert mode)
- cc delete whole line and go into Insert mode
- c$ delete from cursor to end of line and go into Insert mode
- caw change (delete and go to insert mode) whole word that cursor is in
- cc change the entire line (to to Insert mode)

Lesson Two:
- CTRL g to see cursor line number location
- G go to bottom of file
- gg go to top of file
- line number G to move to line number in file
- : [num] go to num line number in file (similar to [num] G command, as above)

Lesson Three:
- / to search
- n after search word to find next occurance of word
- N after search word to find previous occurance of word
- CTRL r CTRL w after using / will insert word under cursor into search
- * will search all words like one under cursor

Lesson Four:
- % to find matching ), ], } parentheses
- :s/old/new to sustitute one occurance of old word with new word
- :s/old/new/g to substitute all the old words with the new words in line
- :%s/old/new/gc to substitute all old words with new worlds in file, one-at-time
- vawp paste yanked word onto word cursor is under, replaceing it

Lesson Five:
- :! command to execute external (terminal) command
- :w file.txt to save file
- v for visual mode
- v :w or d will save text to new file or delete selected text
- :r filename will retreve text from filename into current doc at cursor

Lesson Six:
- o to insert line below cursor, enter Insert mode
- O to insert line above cursor, enter Insert mode
- a to insert text AFTER the cursor
- e to move forward via end of word
- use v, y, and p to Visual mode, copy and paste
- yw to copy word
- yy to copy line
- :set hlsearch highlighs search words with /word
- :set ic to search words and ignore case
- :set nu to show line numbers
- :set nonumber to hide line numbers

Lesson Seven:
- :help to enter help mode
- CTRL w CTRL w to jump from one window to another
- :q to close help window
- :help w for help on w command
- :help vimrc-intro
- CTRL d <TAB> for tab completion of command (:e CTRL d <TAB> = :edit)

BONUS:
- CTRL v then arrows, followed by SHIFT i or SHIFT a to column select and
  insert
- CTRL d to advance down by half-page
- CTRL u to advance up by half-page
- M for move cursor to middle of file view (H for top, L for bottom)
- di> to delete in between < > brackets. Can also do ci) for between ()

Buffers:
- CTRL d for TAB completion (like filenames)
- :e filename to open a buffer for filename
- :vsplit or :vs to split windows vertically
- :buffers to see list of buffers
- :bufferN where N is number of buffer to switch to (:bN flying!)
- CTRL w w to switch windows
- Shift CTRL 6 to alternate between 2 different buffers in same window
- use :bn and :bp for cycling through next and previous buffers (sprinting)

Windows (similar to buffers):
- :split splits the current window, adding window with copy of current work
- :new splits the current window, adding an empty window, best approach*
- :vsplit and :vnew do the same thing above, but windows are side by side
- CTRL w CTRL w or CTRL w w switches between windows
- :close closes the current working window
- :only closes all windows except the working window
- :qall quits all windows, unless there are changes
- CTRL w K or J moved windows up and down, respectively 
- vim -o one.txt two.txt three.txt opens all files in separate windows
	- vim -O does this vertically

Vimdiff
- vimdiff one.txt two.txt starts two windows side-by-side for comparision
- :diffsplit two.txt or :veritcal diffsplit makes side-by-side comparision windows
- ]c or [c to jump to changes in the vimdiff

Vimgrep
While in vim, say vim .
- :vimgrep /findthistext/ * will find the text in multiple files
- :cnext for next occurance of find
- :cprev for previous occurnace of find
- @: to repeat command

Tabs (yes they are a thing):
- :tabe make a new tab
- gt go to next tab
- gT got to previous tab

Nvim (and also general Vim) Advance:
- nvim . (for the whole directory to open)
- :vs to split vertically (buffers!)
- :e TAB to see other files/directories (this can be . directory too)

Repeating commands and movements (super advance recording):
This works best if you set in vimrc: xnoremap p pgvy
- qx to start recording actions (actions saved under letter 'x')
- q to stop recording actions
- @x to repeat recorded action saved in letter 'x'
- @@ to repeat most recently saved recorded action
(Example case):
Repeating replacing (pasting) one word with another individually using search
    - (after yanking the word you want to paste over other word)
    - * search with cursor over word you want to replace (overwrite)
    - qx to start recording actions and movements
    - vawp to paste new word over older word
    - n to search to next occurance of old word in file
    - q to stop recording actions and movements
        - this recorded movement is:
            1. paste over old word with new word
            2. since you were in search mode, n advances to next occurance word
    - @x or @@ to repeat saved, previous, recorded action
    - repeat the above command to repeat as many times as you want 

