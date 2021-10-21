from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.indeed.com/q-python-l-Louisville,-KY-jobs.html?vjk=9f51d0dd03678c14&advn=3912603309577834').text
# print(html_text)
soup =  BeautifulSoup(html_text, 'lxml')

job = soup.find('td', class_= 'resultContent')
job_result = job.find('h2', class_= 'jobTitle jobTitle-color-purple')
job_hiring = soup.find('td', class_ = 'shelfItem urgentlyHiring')

company_name = job.find('span', class_ = 'companyName').text
company_position = job_result.find('span').text
hiring = job_hiring.find('div', class_ = 'urgentlyHiring').text

#skills = job.find()

print(company_name)
print(company_position)
print(hiring)


