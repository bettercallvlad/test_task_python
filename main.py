import csv
import logging

WORDS_SECURITY = ['работ', 'серви']
WORDS_REFUNDS = ['верну', 'возвр', 'деньг']
WORDS_TROUBLESHOOTING = ['пробл', 'ошибк', 'непра', 'забыл', 'баг']
WORDS_ACCOUNT = ['аккау', 'учетн', 'подпи', 'автор', 'логин']
WORDS_ADVERTISING_AND_COLLABORATION = ['сотру', 'рекла']
WORDS_LIMIT =['лимит', 'огран', 'увели']
WORDS_PAYMENTS = ['плате', 'оплат', 'средс']
WORDS_FEATURES = ['функц']

def function (words: list, word: list) -> bool:
	for elem in word:
		for i in words:
			temp = i[:5].lower()
			if elem == temp:
				return True
	return False

def list_to_str(lst:list) -> str:
	rez = ''
	for i in lst:
		rez+=i+" "
	rez += "\n"
	return  rez
def setup_logging():
    logging.basicConfig(filename="other.log",encoding= 'UTF-8', level=logging.INFO, format="%(message)s")



def sorter(filename: str) -> None:
	"""
	Функция получает на вход имя файла с несортированными сообщениями.
	Сортирует сообщения из файла и помещает их в файлы: Security (Безопасность), Refunds (Возврат среств),
	Troubleshooting (Устранение неполадок), Account (Учетная запись), Advertising_and_Collaboration
	 (Реклама и сотрудничество), Limits (Лимиты), Payments (Платежи), Features (функции)
	:param filename: имя файла с несортированными сообщениями

	ТУТ БУДУТ ТЕСТЫ
	"""
	setup_logging()
	with open(filename, encoding='utf-8') as f:
		data = csv.reader(f, delimiter=',')
		for row in data:
			row = row[0].split()
			# print(row)
			# break
			if function(row, WORDS_SECURITY):
				with open("txt\\security.txt", "a+", encoding="UTF-8") as f1:
					f1.write(list_to_str(row))
					continue
			if function(row, WORDS_REFUNDS):
				with open("txt\\refunds.txt", "a+", encoding="UTF-8") as f2:
					f2.write(list_to_str(row))
					continue
			if function(row, WORDS_TROUBLESHOOTING):
				with open("txt\\troubleshooting.txt", "a+", encoding="UTF-8") as f3:
					f3.write(list_to_str(row))
					continue
			if function(row, WORDS_ACCOUNT):
				with open("txt\\account.txt", "a+", encoding="UTF-8") as f4:
					f4.write(list_to_str(row))
					continue
			if function(row, WORDS_ADVERTISING_AND_COLLABORATION):
				with open("txt\\advertising_and_collaboration.txt", "a+", encoding="UTF-8") as f5:
					f5.write(list_to_str(row))
					continue
			if function(row, WORDS_LIMIT):
				with open("txt\\limit.txt", "a+", encoding="UTF-8") as f6:
					f6.write(list_to_str(row))
					continue
			if function(row, WORDS_PAYMENTS):
				with open("txt\payments.txt", "a+", encoding="UTF-8") as f7:
					f7.write(list_to_str(row))
					continue
			if function(row, WORDS_FEATURES):
				with open("txt\\features.txt", "a+", encoding="UTF-8") as f8:
					f8.write(list_to_str(row))
					continue
			else:
				logging.info(msg=str(list_to_str(row)))

if __name__ == '__main__':
	sorter("user_support_letters.csv")
