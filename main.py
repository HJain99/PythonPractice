from general import *
from domain_name import *
from get_ip_address import *
from nmap import *
from robots_txt import *
from whois import *

Root_dir = 'sites'
create_dir(Root_dir)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip = get_ip_address(url)
    nmap = get_nmap('-F', ip)
    robots = get_robots_txt(url)
    whois = get_whois(url)
    create_report(name, url, domain_name, nmap, robots, whois)


def create_report(name, full_url, domain_name, nmap, robots, whois):
    project_dir = Root_dir + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/' + 'full_url.txt', full_url)
    write_file(project_dir + '/' + 'domain_name.txt', domain_name)
    write_file(project_dir + '/' + 'nmap results.txt', nmap)
    write_file(project_dir + '/' + 'robots.txt', robots)
    write_file(project_dir + '/' + 'whois.txt', whois)

site_name = input("Enter the name of the site: ")
site_url = input("Enter the full url of the site: ")
gather_info(site_name, site_url)
