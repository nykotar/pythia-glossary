import os
import re
import yaml
import praw

# REMOVE BEFORE DEPLOY
from dotenv import load_dotenv
load_dotenv()

TERMS_DIRECTORY = './terms'

def get_yaml_files():
    """Retrieves all YAML files."""
    return [f for f in os.listdir(TERMS_DIRECTORY) if f.endswith('.yaml')]

def read_yaml_file(file):
    """Reads a YAML file."""
    with open(f'{TERMS_DIRECTORY}/{file}', 'r') as f:
        return yaml.safe_load(f)

def normalize_string(string):
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)  # Remove special characters
    string = string.replace(' ', '_').replace('-', '_')
    return string

def format_term(term):
    """Formats a term for the wiki page."""
    page = []
    page.append(f'# {term["name"]}  ')
    page.append(f'## Definition  ')
    page.append(f'{term["definition"]}  ')
    if len(term["aliases"]) > 0:
        page.append(f'## Aliases  ')
        page.append(f'{", ".join(term["aliases"])}  ')
    return '\n'.join(page)

def build_glossary(terms):
    """Builds the glossary page."""
    term_keys = list(terms.keys())
    term_keys.sort()

    last_letter = ''
    page = []
    page.append('# Glossary  ')
    page.append('## Terms  ')
    for term in term_keys:
        if term[0].upper() != last_letter:
            last_letter = term[0].upper()
            page.append(f'\n### {last_letter}  ')
        page.append(f'- [{term}]({terms[term]})  ')
    return '\n'.join(page)

def update_page(reddit, wiki_page, content):
    """Updates (or creates) a wiki page."""
    subreddit = reddit.subreddit(os.environ['REDDIT_SUBREDDIT'])
    subreddit.wiki[wiki_page].edit(content=content)

def disable_page(reddit, wiki_page):
    """Disables a wiki page."""
    subreddit = reddit.subreddit(os.environ['REDDIT_SUBREDDIT'])
    subreddit.wiki[wiki_page].mod.update(listed=False, permlevel=0)

def main():
    # Initialize Reddit client
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_CLIENT_SECRET'],
        user_agent=os.environ['REDDIT_USER_AGENT'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD']
    )

    terms = {}
    terms_normalized = []

    # Process all YAML files
    yaml_files = get_yaml_files()
    for file in yaml_files:
        data = read_yaml_file(file)
        update_page(reddit,
            f"glossary/{normalize_string(data['name'])}",
            format_term(data)
        )

        normalized_name = normalize_string(data['name'])
        terms_normalized.append(normalized_name)

        url = f"https://reddit.com/r/{os.environ['REDDIT_SUBREDDIT']}/wiki/glossary/{normalized_name}"
        terms[data['name']] = url
        for alias in data['aliases']:
            terms[alias] = url

    # Update the glossary page
    glossary = build_glossary(terms)
    update_page(reddit, 'glossary', glossary)

    # Disable deleted terms
    wiki_pages = []
    for page in reddit.subreddit(os.environ['REDDIT_SUBREDDIT']).wiki:
        if page.name.startswith('glossary/') and page.name != 'glossary':
            wiki_pages.append(page.name)
    
    for page in wiki_pages:
        if page[9:] not in terms_normalized:
            disable_page(reddit, page)

if __name__ == '__main__':
    main()