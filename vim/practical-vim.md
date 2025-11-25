# Practical Vim Notes

These notes are taken from *Practical Vim* by Drew Neil.

## Opening and Exploring files
This would look something like this:

    vim file1.txt file2.txt
    :new
    :e filename.txt
    <CTRL-w w>

Where the `<CTRL-w w>` cycles through each window. Note that you can also use `<CTRL-w j>`, or k,h,l etc. (see `:h window-move-cursor`) if vimrc is set correctly. Since each window is also a buffer, you can see and change buffers via:

    :ls
    :bn or :bp or :b filename.txt

You can explore to open more in separate windows via:

    :Sexplore

To close current window use `:cl` and to close all but current window use `:on`. To resize current window use `<CTRL-w> =`, `<CTRL-w>_`, and `<CTRL-w>|`. See `:h window-resize`. If lost, use `<CTRL-g>` to see which file you are editing.

## Moving
The most important commands to learn in Vim.

From fast to slow, decending order, of movements:

    gg G
    /search n or N
    Nj or Nk
    _ or 0 and $
    I A
    f to move
    t to act (use with ct{char} or vt{char} or yt{char} or dt{char})
        use ; and , to move about f/t commands
    % jump between matching ([{''}])
    W B or E gE these are true words
    w b or e ge
    gj or gk down up via display line
    
You can quickly search word under cursor by typing `*`. Don't forget that you can *use /search in Visual Mode as well as with motion commands*, like `v/search` or `c/search` or `y/search` or `d/search`.

You can always backtrack your changes, via `g;` or `g,` which moves cursor to previous (newest) change (when user was in Insert Mode). This is jumping the cursor in the document through the change list.

## Editing in Normal Mode
General rule: use `d{motion}` with *a* commands like `daw`, and `c{motion}` with *i* commands like `ciw`. 

Ninjas! Use commands `d`, `c`, `y`, `v` with `/`, `f`, `t`, or `i`, `a`.

    d a w       or      d /     d f
    c i w       or      c /     c f
    y i w       or      y /     y t
    v i w       or      v /     v t

When yanking, deleting, pasting, ensure to use visual mode to highlight word you want to paste on top of, instead of deleting the word. For example:

    yiw
    move to word to paste over
    v{motion, like e}
    p

This ensures not to clobber your registers. Alternatively use the special `"0p` command to paste from the special *yank "0 register*.

## Editing in Insert Mode
One of the niftiest tricks is to *backspace while in Insert Mode* with `<CTRL-w>`. This only works in Insert Mode, but super useful.

You can insert odd characters while in Insert Mode by using *Digraphs*, see `:h digraph-table`. While in Insert Mode type `<CTRL-k>{char1}{char2}` where the `{chars}` are based on the table:

    Ω   W*
    μ   m*
    π   p*
    √   RT
    °   DG

If you don't know the visual character then, with cursor over it, type `ga`.

## Visual Mode
You can use `v`, `V`, or `<CTRL-v>` (block mode) for Visual Mode. When in Visual Mode you can swap between highlight ends with the `o` command. Less useful, when in Normal Mode, you can use `gv` to reselect the previous highlights.

### Visual Mode, block
Remember that when in Visual Mode (like block mode), you need to use *shift i* or *shift a* to edit the lines.

One of the most useful tricks is to use block mode to increment numbers. For example:

    - 1                 Then g <CTRL-a>     - 1
    - 1     <CTRL-v>                        - 2
    - 1         |                           - 3
    - 1         |                           - 4
    - 1         |                           - 5

See `:h v_g_CTRL-a` for specifics.

## Command, Search and Terminal window
You can see *list of searchs* with `q/`, which you can select. Likewise you can use `q:` to access the *previous commands list*.

You can run shell commands with `:shell` or can run one off shell commands via `:!ls`. Think that you want to see the results of written script, you can do any of the following:

    :shell
        python3 script.py
    :!python3 % (% is shorthand for current file)
    :terminal python3 script.py

All of which you can exit with `exit` at anytime.

## Macros
Start macros in correct cursor beginning and ending position. Use `n` (from search), `0`, or `gg` to start macro, and use `w`, `b`, `e`, `ge` commands for moving while recording the macros. To record macros use the `q` comamnd followed by the register to save it. Then to stop recording hit `q` again. To play back the macro call teh register with `@` command and repeat as needed with `@@` command. Think of something like this:

    qa (save macro in register a)
    make changes and moves
    q
    move
    @a
    move
    @@ to repeat
