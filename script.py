# read URL of the website
import requests
import json
import csv


def run():
    print_welcome()
    website_url = read_user_input()
    for strategy in strategies:
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
    with open("results.csv", "a", newline='') as file:
        headers = ['lighthouse fetchTime', 'form factor', 'overall score', 'speed_index', 'first_contentful_pain',
                   'first_meaningful_paint', 'time_to_interactive']

        rows = [report['lighthouseResult']['fetchTime'],
                report['lighthouseResult']['configSettings']['formFactor'],
                report["lighthouseResult"]["categories"]["performance"]["score"] * 100,
                report["lighthouseResult"]["audits"]["speed-index"]["score"] * 100,
                report["lighthouseResult"]["audits"]["first-contentful-paint"]["score"] * 100,
                report["lighthouseResult"]["audits"]["first-meaningful-paint"]["score"] * 100,
                report["lighthouseResult"]["audits"]["interactive"]["score"] * 100]

        csv_writer = csv.writer(file)

        with open('results.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if headers == row[0]:
                    csv_writer.writerow(headers)
                    csv_writer.writerow(rows)
                else:
                    csv_writer.writerow(rows)

        csv_writer.writerow(headers)
        csv_writer.writerow(rows)


if __name__ == '__main__':
    pagespeed_base_url = 'https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    strategies = ["mobile", "desktop"]
    run()
