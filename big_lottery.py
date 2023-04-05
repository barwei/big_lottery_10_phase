import bs4
import requests

# post的參數


def post_parameter(phase):
    my_data = {"__EVENTTARGET": "", "__EVENTARGUMENT": "", "__LASTFOCUS": "", "__VIEWSTATE": "71XJ1TCsF77mQcbHqA1YlYMDTzGNPipbD4VqM01x/hcC5jZK7wGcWFYRLgZFm9VzHWYID52b1W7S3kHUH6ne1MZzFuq/EI/5W31qrC6sAgnumF4cjixed7NsvnDGgRUIT2rtAVJ9O10YZrfd+QN6YwdnNGaxID5xoJkCUSYI/LNX3ZFLAUy/d/BmfwRmZqCy8Th6wdnFvnvOXViO7t7acqscxcoeYgXM4B7i+n2g8EBIoPHbhKkdMEo9Lz1/UmQFqj+v0wOeW1lWy5FlIyh3QofCM5E01tOkS0S9OBjHODwzXy0RLVfxMPGhDFH2MqNFx6+XUdcBd4QAJhx9QoymC1E47KHm9z/YGlNpo64oNepamqddE3aL+KgDY/EIJQ9AErAgjrK2B0JNQZkd3RRkH+R6E3wBxnqeEGXQz+dNIBeomge3iheJ+R/i7HDlXZqkCAyzg/eP5Me7NkiTc+kEbIm+J0bLItBRsL7eASKD8DjSXj9LdOZ988hrJYIMpd3+v6sb7VldObEJpk1mG5jAet4did40/4uFnOHQhiKBCRUnVRE/9QcapMjIzCO1F5tSYF0ssRZFjIKUYRMjpPWM3giDbTd9JmV2qlf8t1550FPSA9tsxMlvf2VMByBjuaLcsarB+1MzX8rOgbJaqsD3qSZTOjkp8rgxkrecJvdsFw85LRXzpkd1oAlyplCYAcOJGlzIUQ0NaPcSpDDzTozrbJvBUCOpCG79Gix2Iixx/37WiZHVognGAfmE9kSDpo7B3MJ0NygKq1F1Q/gPgPRVqpGe5QeBmpTp+zIlWG0mXUCjU1zSssKatwm74gLOtxaVsgKXLzUsSvFb9YFFHwOuPTL5N97+5pZvdbXUxFLqavQKbOvm3MhxUf6QgpsyWt6rTMUSZI9z2UvrWCNcTUzn/lyhoBoxtV5CXAoG/VhzM9Bo4gb5sbgIXsPTRKCwEBCUq4uLGzBUsw+M/WYBZGThk1t3EMC29zgks/CaekdIapL1+2oIX0kADFzJ45QI18O7H+K9JMfxU50ZnpJiO2sr1j2xLih0XjqVClCo/nt2ppfh4qDvtVEAnXnHg3ZGRt/M+JLKqsNetcpe8YQjReY6Wh0JpJg/MYO4OXqtwB1RcV9mo9Pz5dn5ZJvcZRGGNuSTOsMneg70C0COOZkeybxV+Ddb2e6H3rypmChQUAIYQXU1XJZqAL9xf4lCYVePQjZre6sU4k2/vYAWOX2MxguP3sJQ63FBzVwrdtmRL+M2ta+dBl9vUYnDSMM9/+hsXcHccunII+wMYOt29xh7MTKCHiUd8hQ=",
               "__VIEWSTATEGENERATOR": "11E838D2", "__EVENTVALIDATION": "pjQ6vqIyWh8/R3RfPfI2Ae5DnpNSWdDm7u1AqVYf1GlhaaXRgzE5LSLkpx0SH922yb78NYw5IVeJ3/9+Lfn6k8Kwl6OD3WFymcOfPjjfT36KiCLEj2QulM0gKESTYvTWjHqYOk18H4vYLVpK2nDqwuUIjpB91tWQvI0lEBPQoFuhXMvlFNi3leTpD4neaLh1/exP+4inSUeX8vRJHDeNZPtWpYThKZnGtLTXYBkI+ONDWqb0bqKgxQguk9FECMvZdX3GkYldTgxGRFXgaRmzW3VTsOdsNqQ9MaoGOevfnxaXtNQe3TIQvPf4Xkn0m4fEqpZqfRQQzOI2HKxqfTaqvef9f6vbPDPT/97+0NGh/204V01Dyj4NMrLQUg+i/rGpKiC/LZKU0yTvTGzC3oXCtxaS9M//fS36sY3+lg1LS9ok6ihC7FXeJKxveh94HTsnuOPBtYQ0zfAzLoRvAbjKFrRBCk6Y6EzkLizmytGcTfpfLehbJMK6UHWLTV2MomKCZMt7DeDzXkumOy6uzkCIQuGvroiUCiEojZa6jMdIRjC5Ep5SAN9Kbbe4XSK4a9YgDLBJY4SCLYvwaCR8d4+Ftzu+GEvXnR+y5dAQsqn5Q1g9BLjVkcBdtcudd5e2K9qSwIPXSY80q597iCABXKONU5DXcnffWodQoGhCQWm8hwezqQvU", "forma": "請選擇遊戲", "Lotto649Control_history$chk": "radNO", "Lotto649Control_history$txtNO": "112000038", "Lotto649Control_history$btnSubmit": "查詢"}
    my_data["Lotto649Control_history$txtNO"] = str(phase)
    return my_data

# 篩選出當期的號碼，並存入results_numbers list，list 是copy by reference，所以輸入的list值也會跟著改
def phase_numner(results_num, soup_object):
    for number in range(1, 8):
        result_soup = soup_object.select(
            "#Lotto649Control_history_dlQuery_No{}_0".format(number))
        numbper_position = int(result_soup[0].text)-1
        results_num[numbper_position] += 1
    return 0

# 將結果印出每十個換行一次
def disply_result(results_num):
    for i in range(1, 50):
        if i % 10:
            print("[{:02d}] {}".format(i, results_num[i-1]), end="\t\t")
        else:
            print("[{:02d}] {}".format(i, results_num[i-1]))
    return 0


def main():
    # 宣告最後結果的list
    results_numbers = []
    for i in range(49):
        results_numbers.append(0)

    # 將今年期數的數字做統計
    for phase_num in range(112000001, 112000037):
        my_data = post_parameter(phase_num)
        # post大樂透網站獲得當期html code
        lottery_history = requests.post(
            "https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx", data=my_data)
        result_text = lottery_history.text
        # 轉換為BeautifulSoup物件
        soup = bs4.BeautifulSoup(result_text, "lxml")
        phase_numner(results_numbers, soup)

    disply_result(results_numbers)


main()
