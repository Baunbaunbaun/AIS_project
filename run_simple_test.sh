#!/bin/sh

echo "Run simple test"

pwd=$(pwd)

echo $pwd

osascript  <<EOF
tell app "Terminal"
  do script "cd $pwd ; python3 shore_connection.py"
end tell
EOF

osascript  <<EOF
tell app "Terminal"
  do script "cd $pwd ; python3 simple_test.py"
end tell
EOF
