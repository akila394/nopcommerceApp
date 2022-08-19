REM pytest -v -m "sanity and regression" --html=Reports\report.html testCases  --browser chrome
REM pytest -v -m "regression" -n=2 --html=Reports\report.html testCases  --browser chrome
REM pytest -v -n=2 --html=Reports\report.html testCases\test_searchCustomerByEmail.py  --browser chrome
pytest -v  -n=2 --html=Reports\report_chrome.html testCases\test_customers.py  --browser chrome
pytest -v  -n=2 --html=Reports\report_firefox.html testCases\test_customers.py  --browser firefox



