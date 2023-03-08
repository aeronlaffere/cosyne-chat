# Cosyne Chat

This is a Python application which uses the ChatGPT API in combination with [Langchain](https://langchain.readthedocs.io/en/latest/) to power a question answering interface for the [COSYNE 2023 conference](https://www.cosyne.org/). 

Users can ask the ChatGPT about abstracts submitted to the conference and receive a summary answer with details for the relevant poster sessions.

The application relies on data scraped from [WorldWideNeuro](https://www.world-wide.org/cosyne-23/) and uses [Streamlit](https://streamlit.io) for UI and hosting.

No guarantee is made for accuracy. This is a large language model application so answers can sometimes be hallucinatory, although effort has been made to reduce this. Ultimately, it's just a bit of fun &mdash; so enjoy!