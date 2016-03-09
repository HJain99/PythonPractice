import os

def get_ip_address(url):
    command = 'ping ' + url
    process = os.popen(command)
    results = str(process.read())
    startmarker = results.find('[')
    endmarker = results.find(']')
    return results[startmarker+1:endmarker]
