# Tmux Instant

These are the order of common commands to for using **tmux**.

The default is CTRL b , however it can be changed to the easier CTRL a.

## Order of commands

- tmux new -s dev
    - the 'dev' is just a name you can give it
- CTRL b % split pane horizontally
    - CTRL b " split pane vertically
- CTRL b o switch between split panes
    - CTRL b arrow keys work too
- CTRL b x close pane
    - CTRL d does it faster
- tmux ls will list all the sessions
- tmux kill-session will close all sessions

### Having the process keep running

The cool thing about tmux is that you can have a session stay running, even if you detach from it. 

- CTRL b d to detach, but process still runs in background
- tmux attach will reinstate all panes
- tmux ls will list all the sessions
- tmux kill-session will close all sessions
