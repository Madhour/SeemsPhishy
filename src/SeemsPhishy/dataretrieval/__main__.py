from sys import exit
import argparse

from enumeration import Enumeration
from ocr import TextParser

seemsphishy = """

             _________         .    .
            (..       \_    ,  |\  /|
             \       O  \  /|  \ \/ /
              \______    \/ |   \  / 
   Seems Phishy! vvvv\    \ |   /  |
                 \^^^^  ==   \_/   |
                  `\_   ===    \.  |
                  / /\_   \ /      |
                  |/   \_  \|      /
                         \________/
                         
"""

if __name__ == "__main__":
    # ascii-art
    print(seemsphishy)

    # argument
    # takes organization name and returns dict-object with title-text
    args = argparse.ArgumentParser(description="Main", formatter_class=argparse.RawTextHelpFormatter,
                                   usage=argparse.SUPPRESS)
    args.add_argument("-e", "--enumerate", dest="enumeration", type=str, help="Target company name for enumeration",
                      required=True)
    args = args.parse_args()
    # argument handler
    try:
        # enumeration
        if args.enumeration:
            company_enum = Enumeration(args.enumeration)
            results = company_enum.get_files()
            print(TextParser(results).convert_files())

    except KeyboardInterrupt:
        print("[MAIN] Closing...")
        exit(0)
