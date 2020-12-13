
rem "rem denotes that this line is a comment"

rem ******************running on chrome***************************
pytest -s -v -m "sanity or regression" testCases
rem pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases
rem pytest -s -v -m "sanity" --html=Reports\report.html testCases
rem pytest -s -v -m "regression" --html=Reports\report.html testCases

rem ******************running on FF***************************
rem pytest -s -v -m "sanity or regression" --html=Reports\report.html testCases --browser edge
rem pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases edge
rem pytest -s -v -m "sanity" --html=Reports\report.html testCases edge
rem pytest -s -v -m "regression" --html=Reports\report.html testCases edge



