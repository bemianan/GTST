Think of **tmux** (Terminal Multiplexer) as a window manager for your Linux terminal. ==It allows you to run multiple terminal sessions inside one window, keep processes running even if you disconnect from a server, and split your screen into multiple "panes."== 

**1. Getting Started**

If you don't have it installed, you can grab it using your package manager:

- **Ubuntu/Debian:** `sudo apt install tmux`
- **Fedora/RHEL:** `sudo dnf install tmux` 

To start a new session, simply type:

bash

```
tmux
```

Use code with caution.

Or, better yet, give your session a name so you can find it easily later:

bash

```
tmux new -s my_session
```

Use code with caution.

**2. The "Prefix" Key**

Most tmux commands require a **Prefix** to tell tmux, "Hey, listen to me, not the program running inside."

- **Default Prefix:** `Ctrl` + `b`
- **How to use it:** Press `Ctrl` and `b` at the same time, release them, and then quickly press the command key (like `c` for a new window).
---

**3. Key Shortcuts Cheat Sheet**

| Action                               | Shortcut (after `Ctrl` + `b`)        |     |
| ------------------------------------ | ------------------------------------ | --- |
| **Windows (Tabs)**                   |                                      |     |
| Create a new window                  | `c`                                  |     |
| Switch to next/previous window       | `n` / `p`                            |     |
| Switch to a specific window          | `0`, `1`, `2`...                     |     |
| Rename current window                | `,` (comma)                          |     |
| **Panes (Splits)**                   |                                      |     |
| Split screen vertically              | `%`                                  |     |
| Split screen horizontally            | `"`                                  |     |
| Move between panes                   | `Arrow Keys`                         |     |
| Close current pane                   | `x` (then `y` to confirm)            |     |
| **Session Control**                  |                                      |     |
| Detach (leave running in background) | `d`                                  |     |
| List all active sessions             | (Run `tmux ls` in a normal terminal) |     |
| View all keybindings                 | `?`                                  |     |

---

**4. Why Use It?**

- **Session Persistence:** If you're working on a remote server via SSH and your internet drops, your work isn't lost. Just log back in and type `tmux attach` to pick up exactly where you left off.
- **Multitasking:** You can have your code editor in one pane, a log file in another, and a database prompt in a third—all in one terminal window.
- **Background Tasks:** You can start a long-running script (like a backup), detach from the session (`Ctrl+b`, then `d`), and close your laptop. The script will keep running on the server. 

**Pro Tip: Scrolling**
In tmux, you can't just use your mouse wheel to scroll by default. You have to enter **Copy Mode**: 

1. Press `Ctrl + b` then `[`.
2. Use the `Arrow Keys` or `Page Up/Down` to scroll.
3. Press `q` to exit and go back to typing. 

For more advanced customization, you can create a `~/.tmux.conf` file to change the prefix key or enable mouse support. Check out the [tmux GitHub Wiki](https://github.com/tmux/tmux/wiki) for a deep dive. 