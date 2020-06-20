#!/usr/bin/env bash
[ -e /tmp/fifo_3 ] || mkfifo /tmp/fifo_3
exec 3<> /tmp/fifo_3
rm -rf /tmp/fifo_3
adb devices | grep "^127" | awk '/^127/{ print $0 }'  >&3
find  -name "C:\\Users\\lenovo\\PycharmProjects\\app\\seleniumhub\\test_case\\xueqiutask\\test_search.py" | {
  while read file; do
    read udid <&3 && {
      echo udid=$udid
      udid=$udid pytest $file
      echo $udid >&3
      } &
    done
    wait
}
exec 3<&-
exec 3<&-

