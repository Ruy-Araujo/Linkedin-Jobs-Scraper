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

    1. Fill in the **LINKEDIN_COOKIES** and **CSRF_TOKEN** parameters with those from the platform see [how to generate cookies and csrf-token](#cookies)

    2. Execute the main.py script, passing the search filters as arguments:

    ```python3
    python main.py --keywords 'Data Engineer' --location 'Canada' --pastdays 15
    ```

    Parameters:  
    `keywords`: Keywords to filter job listings.  
    `location`: Location where job listings will be searched.  
    `pastdays`: Number of days to search for job listings.  

The scraper will extract job data from LinkedIn Jobs and save it in a JSON file in the project directory.

## <a id="cookies"></a>How to generate LinkedIn cookies

<img src="media/get_cookies.gif" alt="tutorial">

1. Access the LinkedIn Jobs website.

2. Open the browser console (F12) and go to the Network tab.

3. In the Network tab, press CTRL+F to perform a search and type "csrf-token".

4. Select any item and you will see the "cookie" and "csrf-token" fields in the request header.

5. Rename the **exemple.env** file to **.env** and fill in the **LINKEDIN_COOKIES** and **CSRF_TOKEN** fields with the values obtained in the previous step.
Ex.

    ```env
    LINKEDIN_COOKIES="your_cookies"
    CSRF_TOKEN=ajax:123456789
    ```

## Technical details

The scraper uses the Scrapy framework to parse the HTML of the LinkedIn jobs page and extract information such as job title, company name, location, job description, and date of publication.

The raw data is available [here](data/)

## Contributing

If you want to contribute to this project, feel free to open an issue or send a pull request.
