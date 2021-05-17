#!/bin/sh
INSTALL_PATH=~/.local/bin

if [ ! -e "$INSTALL_PATH" ]; then
    mkdir -p "$INSTALL_PATH"
    echo "Make sure $INSTALL_PATH is in \$PATH."
fi

if [ -e "$INSTALL_PATH/calc" ]; then
    read -r -p "$INSTALL_PATH/calc already exist, delete? [y/N] " response
    case "$response" in
        [yY][eE][sS]|[yY]) 
            rm -rf "$INSTALL_BATH/calc"
        ;;
        *)
            echo "Aborted."
            exit 0
        ;;
    esac
fi

cp calc.py "$INSTALL_PATH/calc"
chmod +x "$INSTALL_PATH/calc"
echo "Done."
