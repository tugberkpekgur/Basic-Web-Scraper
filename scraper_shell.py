import cmd
import argparse
from scraper_core import *
import os

class ScraperShell(cmd.Cmd):
    intro = 'Welcome to the web scraper shell. Type -h or ? to list commands.\n'
    prompt = 'scraper > '
    
    def do_scrape(self, arg):
        """Fetch the content of a URL."""
        args = arg.split()
        url = None
        is_all_tag = False
        class_tag = None

        if '-url' in args:
            try:
                url_index = args.index('-url')
                url = args[url_index + 1]
            except IndexError:
                print("URL not provided. Use -url <URL> to specify a URL.")
                return
        else:
            print("Please provide a URL using -url <URL>.")
            return
        
        if '-all' in args:
            try:
                is_all_tag = True
            except IndexError:
                print("Tags not provided. Use -all <tags> to specify tags.")
                return
        elif '-class' in args:
            try:
                class_index = args.index('-class')
                class_tag = args[class_index + 1]
            except IndexError:
                print("Tags not provided. Use -class <tags> to specify tags.")
                return
        if class_tag and is_all_tag:
            print("Please provide either -all or -class, not both.")
            return
        
        if not url:
            print("Please provide a URL.")
            return
        if is_all_tag:
            content = fetch_url_all_content(url)
        elif class_tag:
            content = fetch_url_content_by_class(url, class_tag, args)
        else:
            content = fetch_url_content(url,args)
        if content:
            print(content)
        else:
            print("Failed to fetch the URL.")

    def do_exit(self, arg):
        """Exit the scraper shell."""
        print("Exiting the scraper shell.")
        return True
    
    def do_clear(self, arg):
        """Clear the screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def do_help(self, arg):
        """Display help information."""
        print("Available commands:")
        print("  scrape -url <url>        Fetch the content of a URL.")
        print("          -<tags>          Fetch tags from the URL.")
        print("          -all             Fetch all tags from the URL.")
        print("          -script          Fetch scripts from the URL.")
        print("          -class <class>   Fetch tags with a specific class from the URL.")
        print("  exit                     Exit the scraper shell.")
        print("  help                     Display this help message.")
        print("  clear                    Clear the screen.")

    def default(self, line):
        if line.strip() in ['-h', '--help']:
            self.do_help('')
        
        else:
            print(f"Unknown command: {line}. Type help for a list of commands.")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web Scraper CLI')
    #parser.add_argument('url', nargs='?', help='URL to fetch')
    
    args = parser.parse_args()
    ScraperShell().cmdloop()
