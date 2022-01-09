from sys import exit
import argparse

from enumeration import ENUMERATION
from textgen import generate2, buildMail

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
	#ascii-art
	print(seemsphishy)
 
	#arguments
	args = argparse.ArgumentParser(description="Main", formatter_class=argparse.RawTextHelpFormatter, usage=argparse.SUPPRESS)
	args.add_argument("-e", "--enumerate", dest="enumeration", type=str, help="Target company name for enumeration", required=False)
	args.add_argument("-g", "--generate", dest="generate", type=str, help="Strings to generate text from", required=False)
	args = args.parse_args()
	#argument handler
	try:
		#enumeration
		if args.enumeration:
			company_enum = ENUMERATION(args.enumeration)
			results = company_enum.getFiles()

		if args.generate:
			text = generate2(args.generate)
			print(text)
			buildMail(text, "TestCorp.")

			
   
	except KeyboardInterrupt:
		print("[MAIN] Closing...")
		exit(0)
