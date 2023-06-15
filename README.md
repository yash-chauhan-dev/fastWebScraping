# fastWebScraping
Scheduled Web Scraping

Here's what each tool is used for:

- **Python 3.9** [download](https://www.python.org/download/) - programming the logic.
- **AstraDB** [sign up](https://dtsx.io/3nQnjz1) - highly perfomant and scalable database service by DataStax. AstraDB is a Cassandra NoSQL Database. [Cassandra](https://cassandra.apache.org/_/index.html) is used by Netflix, Discord, Apple, and many others to handle astonding amounts of data.
- **Selenium** [docs](https://selenium-python.readthedocs.io/) - an automated web browsing experience that allows:
  - Run all web-browser actions through code
  - Loads JavaScript heavy websites
  - Can perform standard user interaction like clicks, form submits, logins, etc.
- **Requests HTML** [docs](https://docs.python-requests.org/) - we're going to use this to parse an HTML document extracted from Selenium
- **Celery** [docs](https://docs.celeryproject.org/) - Celery providers worker processes that will allow us to schedule when we need to scrape websites. We'll be using [redis](https://redis.io/) as our task queue.
- **FastAPI** [docs](https://fastapi.tiangolo.com/) - as a web application framework to Display and monitor web scraping results from anywhere

High-Level Approach:

- Integrate Cassandra with Python, FastAPI, & Celery
- Setup & Configure Astra DB (managed cassandra db)
- Schedule & Offload Tasks with Celery
- Web Scraping Techniques
- Selenium & requests-html to extract & parse data
