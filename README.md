# Anti Enum

This script is designed to provide basic protection against enumeration attacks on a web server. It generates HTML pages with random links from a wordlist, while implementing some security measures to mitigate potential risks.
A hacker that tries to enumerate your server will be overwhelmed with a large number of pages and links, making it difficult to identify the legitimate URLs.

## Features

- Randomly generates HTML pages with links from a wordlist.
- Use an ignored_urls list to exclude URLs from the generation. (Routes used by the web service)
- Implements delay between responses to slow down potential attackers.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

```
git clone https://github.com/davidtchilian/anti_enum.git
cd anti_enum
```


3. (Optional) Modify the configuration files:

- `ignored_urls.txt`: Add any URLs that should be ignored during page generation.
- `wordlist.txt`: Populate this file with the desired URLs to include in the generated pages.
- `anti_enum.py`: Modify the port, server address and delay variables to your desire.

## Usage

1. Start the server by running the following command:`` 

```
python3 anti_enum.py
```


2. Access the generated HTML pages by opening a web browser and navigating to `localhost:<yourport>/url` where `url` corresponds to a URL present in the wordlist.

## Security Improvements

To enhance the security of this script, consider implementing the following measures:

- Replace the basic HTTP server with a more secure and robust server framework (Flask, Django).
- Implement rate limiting to prevent excessive requests from a single IP address.
- Enable HTTPS support to encrypt communication between the server and clients.
- Implement comprehensive logging and monitoring to detect and respond to suspicious activities.
	- You can also redirect or tail the output of the script and treat that as logs.
- Perform security testing and assessments to identify and address vulnerabilities.


## License

This project is licensed under the MIT License.
