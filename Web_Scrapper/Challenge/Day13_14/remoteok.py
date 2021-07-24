import requests
from bs4 import BeautifulSoup

def extract_job(html):
	title = html.find("h3", {"itemprop": "name"}).string
	company = html.find("h2", {"itemprop": "title"}).string
	location = html.find("div", {"class": "location tooltip"}).string
	job_id = html['data-url']
	print(title, company, location, job_id)
	return {
		"title": title,
		"company": company,
		"location": location,
		"apply_link": f"https://remoteok.io{job_id}"
	}


def extract_jobs(url):
	jobs= []
	result = requests.get(url)
	soup = BeautifulSoup(result.text, "html.parser")
	results = soup.find_all("tr", {"class": "job job-"})
	print(results)
	for result in results:
		job = extract_job(result)
		jobs.append(job)
	return (jobs)


def get_jobs(word):
	url = f"https://remoteok.io/remote-{word}-jobs"
	jobs = extract_jobs(url)
	print("RE: ", len(jobs), url)
#	return (jobs)

get_jobs("vr")
