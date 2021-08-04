from urllib.parse import quote
import os

# CONFIGURE HERE
SITE = "palomar"
GITHUB_ACCOUNT = "https://github.com/csit128"
GITHUB_MATERIALS_REPO = "csit128_Intro_DS"

# DO NOT TOUCH BELOW
HUB_SITE = f"{SITE}.cloudbank.2i2c.cloud"
PLACEHOLDER_HUB_SITE = "demo.cloudbank.2i2c.cloud"
PLACEHOLDER_GITHUB_ACCOUNT = "https://github.com/data-8"
PLACEHOLDER_GITHUB_MATERIALS_REPO = "materials-sp20-external"

with open("index_site_configure.html", "r") as f:
    filedata = f.read()

filedata = filedata.replace(PLACEHOLDER_HUB_SITE, HUB_SITE)
filedata = filedata.replace(quote(PLACEHOLDER_GITHUB_ACCOUNT, safe=''), quote(GITHUB_ACCOUNT, safe=''))
filedata = filedata.replace(PLACEHOLDER_GITHUB_MATERIALS_REPO, GITHUB_MATERIALS_REPO)
filedata = filedata.replace("Demo Hub", f"{SITE} Hub".title())
filedata = filedata.replace("Demo Hub", f"{SITE} Hub".title())

site_index_name = f'../{SITE}.html'
with open(site_index_name, 'w') as file:
    file.write(filedata)

os.rename('../index.html', '../index_data8_example.html')
os.rename(site_index_name, '../index.html')
