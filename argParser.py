import argparse


def getArgs():
  parser = argparse.ArgumentParser(description="A steganography tool written in Python, similar to Stegsolve.")
  parser.add_argument('-f', '--file', type=str, required=True, nargs='+', help="path to the image(s)")
  parser.add_argument('-o', '--output', type=str, nargs=1, help="path to directory where you want to save the image(s)")

  args = parser.parse_args()

  return args