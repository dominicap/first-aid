def title(url):
    return call_to_api(url).title

def description(url):
    return call_to_api(url).description

def call_to_api(url):
    call api for url
