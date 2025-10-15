# Tmux Instant

These are the order of common commands to for using **tmux**.
The default is CTRL b, however it can be changed to the easier CTRL a.
Note: To scroll: CTRL b [ then use arrow keys. Press q to quit scroll mode.

## Order of commands

- tmux new -s dev
    - the 'dev' is just a name you can give it

### Panes
- CTRL b % split pane horizontally
    - CTRL b " split pane vertically
- CTRL b o switch between split panes
    - CTRL b arrow keys work too
- CTRL d close pane OR window, DTM favorite
    - CTRL b x close pane or window
- tmux ls will list all the sessions
- tmux kill-session will close all sessions
- CTRL b f <ENTER> will go into search pane mode

### Windows
- CTRL b c new window
- CTRL b w will go into search windows mode
- CTRL b <NUMBER> changes current window to NUMBER window
- CTRL d close pane OR window, DTM favorite
    - CTRL b x close pane or window

### Having the process keep running

The cool thing about tmux is that you can have a session stay running, even if you detach from it. 

- CTRL b d to detach, but process still runs in background
- tmux attach will reinstate all panes
- tmux ls will list all the sessions
- tmux kill-session will close all sessions
