import wxr_parser

parsed_data = wxr_parser.parse('wordpress.xml')
print(parsed_data['posts'][0])
