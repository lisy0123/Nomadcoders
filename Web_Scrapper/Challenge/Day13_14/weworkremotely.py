import requests
from bs4 import BeautifulSoup

def extract_job(html):
	html = html.find_all("a")[1]
	title = html.find("span", {"class": "title"}).string
	company = html.find("span", {"class": "company"}).string
	location = html.find("span", {"class": "region company"}).string
	job_id = html['href']
	return {
		"title": title,
		"company": company,
		"location": location,
		"apply_link": f"https://weworkremotely.com{job_id}"
	}


def extract_jobs(url):
	jobs= []
	result = requests.get(url)
	soup = BeautifulSoup(result.text, "html.parser")
	results = soup.find_all("li", {"class": "feature"})
	for result in results:
		job = extract_job(result)
		jobs.append(job)
	return (jobs)


def get_jobs(word):
	url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
	jobs = extract_jobs(url)
	print("WE: ", len(jobs), url)
	return (jobs)

