#!/bin/bash

# This script provides a convenient way to run pytest with coverage badge generation
# You can source this file or add its contents to your ~/.bashrc or ~/.zshrc

# Alias to run pytest with coverage and badge generation
alias pytest="python test_with_coverage.py"

# You can also add this to your shell configuration by running:
# echo "alias pytest='python /path/to/test_with_coverage.py'" >> ~/.bashrc
# source ~/.bashrc

echo "🎯 Pytest alias configured!"
echo "💡 Now you can just run 'pytest' and it will automatically generate coverage badges."