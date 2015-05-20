SublimeText-Config
==================

Packages, keybindings and settings from my Sublime Text configuration.


# Keybindings

The difference between platforms is mostly changing ctrl (Windows, Linux) by super (Mac).

## Vintage

The Vintage config tries to merge Sublime Text shortcuts with the Vim command mode, without leaving the confort of the home row.

### Useful bindings

````javascript
    //
    // Overlay (use GoTo Anything panel without using the arrow keys):

    // Move right in overlay (open tab)
    { "keys": ["super+l"], "command": "move", "args": { "by": "characters", "forward": true },
        "context": [ { "key": "overlay_visible", "operator": "equal", "operand": true } ]
    },

    // Move down in overlay
    { "keys": ["super+j"], "command": "move", "args": { "by": "lines", "forward": true },
        "context": [ { "key": "overlay_visible", "operator": "equal", "operand": true } ]
    },

    // Move up in overlay
    { "keys": ["super+k"], "command": "move", "args": { "by": "lines", "forward": false },
        "context": [ { "key": "overlay_visible", "operator": "equal", "operand": true } ]
    },

    //
    // Move in search results and go to definition

    { "keys": ["g", "o"], "command": "next_result", "context": [{ "key": "setting.command_mode" }] },
    { "keys": ["g", "O"], "command": "prev_result", "context": [{ "key": "setting.command_mode" }] },

    { "keys": ["g", "d"], "command": "goto_definition", "context": [{ "key": "setting.command_mode" }] },

    //
    // Multiple cursors and moving lines

    // Multiselection (more than one cursor)
    { "keys": ["super+alt+k"], "command": "select_lines", "args": {"forward": false}, "context": [{"key": "setting.command_mode"}] },
    { "keys": ["super+alt+j"], "command": "select_lines", "args": {"forward": true}, "context": [{"key": "setting.command_mode"}] },
    
    // Move lines
    { "keys": ["super+shift+k"], "command": "swap_line_up", "context": [{"key": "setting.command_mode"}] },
    { "keys": ["super+shift+j"], "command": "swap_line_down", "context": [{"key": "setting.command_mode"}] },
````

# Packages

I have the following packages installed:

````
AAAPackageDev                  Rails Partial
All Autocomplete               RSpec (snippets and syntax)
ApplySyntax                    RubyTest
Better Completion              Sass
Copy from Find Results         SublimeERB
EasyMotion                     SublimeLinter
Emmet                          SublimeLinter-jshint
FileBrowser                    SublimeLinter-pylint
GitGutter                      SublimeLinter-ruby
GitSavvy                       SublimeREPL
Gulp                           Sublimerge Pro
I18n_Rails                     Surround
Jasmine                        Terminal
Monokai_Extended               Theme - Gravity
MoveTab                        Theme - Spacegray
Origami                        Trello
PlainTasks                     Vintage Escape
Predawn                        Vintage Surround
Quick_File_Creator             Vintage-Origami
````

if you're using [Package Control](https://packagecontrol.io/installation), you can add any of those names to your `Package Control.sublime-settings` file and after restaring it will be installed automatically.

If you're not using Package Control, you can search for each package and clone it on your Packages folder.

### Essential

1. [All Autocomplete](https://packagecontrol.io/packages/All%20Autocomplete): Extends the default autocomplete to find matches in all open files. By default Sublime only considers words found in the current file.
2. [Emmet](http://emmet.io/): A **ton** of useful stuff for HTML and CSS.
3. [GitGutter](https://packagecontrol.io/packages/GitGutter): Show an icon in the gutter area indicating whether a line has been inserted, modified or deleted.
4. [Origami](https://packagecontrol.io/packages/Origami): Keyboard driven pane management. Split the window however you like! Create new panes, delete panes, move and clone views from pane to pane.
5. [GitSavvy](https://packagecontrol.io/packages/GitSavvy): Full git and GitHub integration with Sublime Text 3. **Nota:** Si por alguna razón están usando Sublime Text 2, pueden probar [SublimeGit](https://packagecontrol.io/packages/SublimeGit).
6. [SublimeLinter](https://packagecontrol.io/packages/SublimeLinter): Interactive code linting framework for Sublime Text 3. It has support for a bunch of languages (provided as separate packages).
7. [Sublimerge Pro](https://packagecontrol.io/packages/Sublimerge%20Pro): The professional, side-by-side tool to diff and merge files and directories right in Sublime Text. Supports Git, SVN and Mercurial.

Honorable mention:

* [PlainTasks](https://packagecontrol.io/packages/PlainTasks): Todo-list plugin for Sublime Text.
* [Copy from Find Results](https://packagecontrol.io/packages/Copy%20from%20Find%20Results): Copy without line numbers

# Preferences

The preferences file it's probably a personal thing, but a few interesting options are:

````javascript
{
    //
    // Exclude patterns so you get cleaner searches
    "file_exclude_patterns": [ /*...*/ ],
    "folder_exclude_patterns": [ /*...*/ ],

    //
    // To use along side origami, to have the split on focus take up 75% of the screen
    "origami_auto_zoom_on_focus": 0.75

    //
    // Vim
    // Have a block caret and start in command mode
    "highlight_line": false,
    "inverse_caret_state": true,
    "caret_style": "phase",
    "vintage_start_in_command_mode": true,
}
````
