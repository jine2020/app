for i in `adb devices |findstr "device$"|awk "{print $1}"`;
do
  echo $i
  udid=$i pytest C:\\Users\\lenovo\\PycharmProjects\\app\\test_xueqiu_node.py &
done