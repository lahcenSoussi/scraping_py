# install http://www.wkhtmltopdf.org depend of your OS, I use Ubuntu.
# install pdfkit

import pdfkit

path_wkhtmltopdf = r'/usr/local/bin/wkhtmltopdf'

#define url of the page
url = 'https://www.python.org/' #choose any url you want

#configure pdfkit options
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

#convert url to pdf
pdfkit.from_url(url, 'out.pdf', configuration=config)
#run this code in terminal, python3 wkhtmltopdf.py