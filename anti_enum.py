from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import random

IGNORED_URLS_FILE = "ignored_urls.txt"
URL_FILE = "wordlist.txt"

# in seconds
MIN_DELAY = 0.1
MAX_DELAY = 0.5

SERVER_ADDRESS = "localhost"
SERVER_PORT = 80

IGNORED_URLS = []
with open(IGNORED_URLS_FILE, "r") as f:
    for line in f.readlines():
        IGNORED_URLS.append(line.strip())

URLS = []
with open(URL_FILE, "r") as f:
    for line in f.readlines():
        URLS.append(line.strip())

print("loaded " + str(len(URLS)) + " URLs")
# print first ten URLs
print("first ten URLs:")
for i in range(10):
    print(URLS[i])

for ignored_url in IGNORED_URLS:
    if ignored_url in URLS:
        URLS.remove(ignored_url)

def generate_html_page(path):
    num_a_tags = random.randint(5, 15)
    html = "<html>\n<body><br>\n"
    for i in range(num_a_tags):
        url = random.choice(URLS).strip()
        html += "<a href=\"" + url + "\">" + url + "</a><br>\n"
    html += "</body>\n</html>\n"
    return html

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("/")[1:][0] not in URLS:
            print("not found: " + self.path.split("/")[1:][0])
            return
        time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        html = generate_html_page(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html, "utf-8"))
        return

def main():
    if len(IGNORED_URLS) == 0:
        print("WARNING: no ignored URLs specified. Continue ? (y/n)")
        i = input()
        if i != "y" and i != "Y":
            print("exiting...")
            print("please specify ignored URLs in ignored_urls.txt")
            sys.exit(1)

    try:
        print("starting server...")
        server = (SERVER_ADDRESS, SERVER_PORT)
        httpd = HTTPServer(server, CustomHandler)
        print("running server...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping server...")
        httpd.socket.close()
        sys.exit(1)

if __name__ == "__main__":
    main()