import tldextract

def extract_domain_name(url):
	extracted = tldextract.extract(url)
	domain = extracted.domain+'.'+extracted.suffix
	return domain
	
