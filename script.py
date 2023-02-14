# read URL of the website
import requests
import json


def run():
    print_welcome()
    performance_report = query_performance()
    create_report(performance_report)


def print_welcome():
    print('Check performance results by providing website URL')


def query_performance():
    website_url = input('enter website URL: ')
    pagespeed_full_url = pagespeed_url + website_url
    print(pagespeed_full_url)
    web_response = requests.get(pagespeed_full_url)

    return json.loads(web_response.content)


def create_report(report):
    print("lighthouse fetchTime")
    print(report['lighthouseResult']['fetchTime'])
    print("form factor")
    print(report['lighthouseResult']['configSettings']['formFactor'])
    print("overall score")
    print(report["lighthouseResult"]["categories"]["performance"]["score"] * 100)
    print("speed_index")
    print(report["lighthouseResult"]["audits"]["speed-index"]["score"] * 100)
    print("first_contentful_paint")
    print(report["lighthouseResult"]["audits"]["first-contentful-paint"]["score"] * 100)
    print("time_to_interactive")
    print(report["lighthouseResult"]["audits"]["interactive"]["score"] * 100)


if __name__ == '__main__':
    pagespeed_url = 'https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    run()
