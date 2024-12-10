import schedule
import time
import utils.rss_parser
import utils.llm

feeds = [
    {'name': 'Morning brew RSS feed', 'url': 'https://feeds.megaphone.fm/MOBI8777994188', 'category': 'Business'},
    {'name': 'BBC UK News RSS feed', 'url': 'https://feeds.bbci.co.uk/news/uk/rss.xml', 'category': 'UK'},
    {'name': 'Marketwatch Feed', 'url': 'https://feeds.content.dowjones.io/public/rss/mw_topstories',
     'category': 'Finance'},
]


def job():
    # Fetch RSS and summarize
    print("Running job...")
    # Initialize an empty list to collect all entries
    all_entries = []
    for feed in feeds:
        # Get the latest RSS entries for the current feed
        print("Fetching " + feed['name'] + "...")
        latest_entries = utils.rss_parser.get_latest_rss(feed['url'])
        # Concatenate the results into the all_entries list
        all_entries.extend(latest_entries)
    # Summarize the entries
    print("Summarizing feeds...")
    summary = utils.llm.summarize(str(all_entries))

    # Convert the summary to audio
    print("Generating TTS output...")
    utils.llm.tts(summary)

    print("Completed RSS summarization.")


schedule.every().day.at("06:00").do(job)
# schedule.every().minute.at(":17").do(job)

# job()

while True:
    schedule.run_pending()
    time.sleep(300)
