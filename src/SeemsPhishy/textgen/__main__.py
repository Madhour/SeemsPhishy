from sys import exit
import argparse

# from enumeration import ENUMERATION
from textgen import generate, build_mail

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

    # arguments
    args = argparse.ArgumentParser(description="Main", formatter_class=argparse.RawTextHelpFormatter,
                                   usage=argparse.SUPPRESS)
    args.add_argument("-g", "--generate", dest="generate", type=str, help="Keywords to generate text", required=False)
    args = args.parse_args()
    # argument handler
    try:

        if args.generate:
            text = generate(args.generate)  # keywords: "keyword1,keyword2,keyword3" all without spaces!
            print(text)
            build_mail(text, "TestCorp.")  # pass generated text and Organization name

    except KeyboardInterrupt:
        print("[MAIN] Closing...")
        exit(0)
