# install http://www.wkhtmltopdf.org depend of your OS, I use Ubuntu.
# install pdfkit

import pdfkit

try:
    path_wkhtmltopdf = r'/usr/local/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # #define url of the page
    url = 'https://docs.qfq.io/en/master/'
    print('Converting page: ', url)
    # #convert url to pdf
    try:
        pdfkit.from_url(url, 'out.pdf', configuration=config)
        print('PDF created successfully!')
    except Exception as e:
        print('Error: ', e)

except Exception as e:
    print('Error: ', e)
