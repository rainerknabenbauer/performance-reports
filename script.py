# read URL of the website
import requests
import json


def run():
    print_welcome()
    website_url = read_user_input()
    for strategy in strategies:
        print("now we are in loop " + strategy)
        strategy_specific_url = build_full_url(website_url, strategy)
        performance_report = query_performance(strategy_specific_url)
        create_report(performance_report)


def print_welcome():
    print('Check performance results by providing website URL')


def read_user_input():
    return input('enter website URL: ')


def build_full_url(website_url, strategy):
    full_url = pagespeed_base_url + website_url + "&strategy=" + strategy
    print("url is: " + full_url)
    return full_url


def query_performance(strategy_specific_url):
    web_response_desktop = requests.get(strategy_specific_url)
    response = json.loads(web_response_desktop.content)
    return response


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
    print("first_meaningful_paint")
    print(report["lighthouseResult"]["audits"]["first-meaningful-paint"]["score"] * 100)
    print("time_to_interactive")
    print(report["lighthouseResult"]["audits"]["interactive"]["score"] * 100)


if __name__ == '__main__':
    pagespeed_base_url = 'https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    strategies = ["mobile", "desktop"]
    run()
