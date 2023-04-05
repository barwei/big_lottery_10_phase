import bs4
import requests

# 宣告最後結果的list
results_numbers = []
for i in range(49):
    results_numbers.append(0)

# get大樂透網站html code
lottery_history = requests.get(
    "https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx")
result_text = lottery_history.text

# 轉換為BeautifulSoup物件
soup = bs4.BeautifulSoup(result_text, "lxml")

# 選擇近十期的號碼，並存入results_numbers list
for phase in range(10):
    for number in range(1, 8):
        result_soup = soup.select(
            "#Lotto649Control_history_dlQuery_No{}_{}".format(number, phase))
        numbper_position = int(result_soup[0].text)-1
        results_numbers[numbper_position] += 1

# 將結果印出每十個換行一次
for i in range(1, 50):
    if i % 10:
        print("[{:02d}] {}".format(i, results_numbers[i-1]), end="\t")
    else:
        print("[{:02d}] {}".format(i, results_numbers[i-1]))
