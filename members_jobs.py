import urllib.request
import requests
import PyPDF2
from bs4 import BeautifulSoup
import datetime


url = 'https://www.icsi.edu/JOBOPPORTUNITIES.aspx'
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")

job_opportunity_for_members = soup.select(
	'#dnn_ctr13100_HtmlModule_lblContent > table > tbody')[0]
job_opportunity_for_members_2_years_above = soup.select(
	'#dnn_ctr12264_HtmlModule_lblContent > ul > table > tbody')[0]
job_opportunity_from_public_advt = soup.select(
	'#dnn_ctr13079_HtmlModule_lblContent > table > tbody')[0]

jobs = [job_opportunity_for_members, job_opportunity_for_members_2_years_above]


def download_file(url):
	local_filename = '/tmp/' + url.split('/')[-1]
	print('Downloading File...', local_filename)
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	print('Downloaded')
	return local_filename

def post_to_jobs(raw, tds, pdf_url, d):
	url = 'https://forum.csclub.co/posts'
	payload = {
		"api_key": "ef759d736fc5495f16fd29eef742e822cd1203c81a9e871eef863b3dc10aad2f",
		"api_username": "vaibhavmule",
		"title": "{} is Looking for Company Secretary in {}".format(
			tds[0].text.strip('\n'), tds[1].text.strip('\n')),
		"raw": raw,
		"category": 5,  # jobs category
	}
	r = requests.post(url, data=payload)
	auto_close_on_expiry_date(1107, d)
	print('response', r.text, r.status_code)

def auto_close_on_expiry_date(t, d):
	url = 'https://forum.csclub.co/t/{}/timer'.format(t)
	payload = {
		"api_key": "ef759d736fc5495f16fd29eef742e822cd1203c81a9e871eef863b3dc10aad2f",
		"api_username": "vaibhavmule",
		'time': d.strftime('%Y-%m-%d %H:%M+05:30'),
		'status_type': 'close',
	}
	r = requests.post(url, data=payload)
	print('response', r.text, r.status_code)


for job in jobs:
	for tr in job.find_all('tr')[1:]:
		tds = tr.find_all('td')
		try:
			d = datetime.datetime.strptime(' '.join(tds[3].text.split()),'%d-%m-%Y')
		except ValueError:
			d = datetime.datetime.strptime(' '.join(tds[3].text.split()),'%d/%m/%Y')
			
		if d > datetime.datetime.now():
			pdf_url = tds[0].a['href']
			file_name = download_file(pdf_url)
			pdfFileObj = open(file_name, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
			pageObj = pdfReader.getPage(0)
			
			if pdfReader.numPages == 2:
				pageObj1 = pdfReader.getPage(1)
				text = pageObj.extractText() + pageObj1.extractText()
			else:
				text = pageObj.extractText()
			text = ' '.join(text.split()).split(':')
			try:
				raw = '{}\n\n**Job Description:**{}\n\n**Eligibility:**{}\n\n**Requirement:**{}\n\n**Salary Details:**{}\n\n**Job location:**{}\n\n**Apply at:**{}\n\n**Expiry Date of Job Posting:** {}\n\n**Source:** Uploaded on {} at [ICSI]({})"'.format(
					text[1].replace(' Job Description', ' ').lstrip(),
					text[2].replace(' Eligibility', ' '),
					text[3].replace(' Requirement', ' '),
					text[4].replace(' Salary Details', ' '),
					text[5].replace(' Job location ', ' '),
					text[6].replace(' Apply at', ' '),
					text[7],
					tds[3].text.strip('\n'),
					tds[2].text.strip('\n'),
					pdf_url)
				post_to_jobs(raw, tds, pdf_url, d)
			except IndexError:
				pass
		

"""
https://forum.csclub.co/t/875/timer
time:2018-03-13 08:39+05:30
status_type:close
"""
