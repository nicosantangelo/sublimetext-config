SublimeText-Config **WIP**
==================

Packages, keybindings and settings from my Sublime Text configuration.


# Keybindings

Platforms

## Vintage

The Vintage config is mostly done to try to merge SublimeText shortcuts without leaving the confort of the home row.

### Useful bindings

````
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

What's in here?

## Package Control

Install stuff

# Preferences

Probably change it