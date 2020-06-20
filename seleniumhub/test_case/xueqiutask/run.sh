for i in `adb devices |findstr "device$"|gawk '{print $1}'`;
do
  echo $i
  udid=$i pytest C:\\Users\\lenovo\\PycharmProjects\\app\\seleniumhub\\test_case\\xueqiutask\\test_search.py &
done