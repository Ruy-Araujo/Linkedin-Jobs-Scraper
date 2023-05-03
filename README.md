[![pt-br](https://img.shields.io/badge/lang-PT--BR-yellowgreen?style=for-the-badge&logo=googletranslate&logoColor=4285F4)](/README.pt-br.md)

# Linkedin Jobs Scraper

This repository contains a LinkedIn jobs scraper written in Python that extracts job data and saves it in JSON files.

## How to use

1. Clone the repository to your local machine:

```bash
    git clone https://github.com/Ruy-Araujo/Linkedin-Jobs-Scraper
```

2. Install the dependencies:

```bash
    cd Linkedin-Jobs-Scraper
    pip install -r requirements.txt
```

3. Configure the exemple.env file:

    1. Fill in the *LINKEDIN_COOKIES* and *CSRF_TOKEN* parameters with those from the platform see [how to generate cookies and csrf-token](#cookies)

    2. The *KEYWORDS* field is a string with the keywords that will be used to filter job listings.

    3. The *LOCATION* field is a string with the location where the job listings will be searched.

4. Run the main.py script

```python3
    python main.py
```

The scraper will extract job data from LinkedIn Jobs and save it in a JSON file in the project directory.

## <a id="cookies"></a>How to generate LinkedIn cookies

1. Access the LinkedIn Jobs website.

2. Open the browser console (F12) and go to the Network tab.

3. In the Network tab, press CTRL+F to perform a search and type "csrf-token".

4. Select any item and you will see the "cookie" and "csrf-token" fields in the request header.

## Technical details

The scraper uses the Scrapy framework to parse the HTML of the LinkedIn jobs page and extract information such as job title, company name, location, job description, and date of publication.

The raw data is available [here](data/)

## Contributing

If you want to contribute to this project, feel free to open an issue or send a pull request.
