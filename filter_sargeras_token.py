import sys
import re


def filter(infilename, outfilename, regex):
    data = open(infilename)
    filtered = open(outfilename,"w")
    for line in data:
        matched = regex.findall(line)
        # print matched
        for str in matched:
            filtered.write("%s\n"%(str))
            # if matched != []:
            # filtered = matched[len(prefix):len(prefix) + token_len]
            # print matched


if __name__ == "__main__":
    # regex=re.compile(r"^<td data-decimals=\"0\" data-type=\"string\" class=\"data  not_null   text \">")
    outfilename = "/Users/yes/ele/about_sargeras/V0.8.0/filtered_tokens"
    token_pattern = re.compile(r'\w+-\w+-\w+-\w+-\w+')
    token_len = len("8ecf17f5-42f9-4287-a9f9-b88db488498d")
    filename = "/Users/yes/ele/about_sargeras/V0.8.0/tokens"
    filter(filename, outfilename, token_pattern)
