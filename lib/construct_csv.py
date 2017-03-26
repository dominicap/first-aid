import csv

descriptions_file = open("../data/txt/link_keywords.txt", "r")
descriptions = list(descriptions_file.read().splitlines())

indexes = []
for description in descriptions:
    if description == '':
        indexes = [index for index, description in enumerate(descriptions) if description == ""]

with open('../data/txt/final/final_data_keywords.txt', 'a+') as file:
    for description in descriptions:
        if not descriptions.index(description) in indexes:
            file.write(description + '\n')

links_file = open("../data/txt/relevant_video_links.txt", "r")
links = list(links_file.read().splitlines())

with open('../data/txt/final/final_data_links.txt', 'a+') as file:
    for link in links:
        if not links.index(link) in indexes:
            file.write(link + '\n')

# with open("../data/txt/relevant_video_links.txt", "r") as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line for line in stripped if line)
#     grouped = zip(*[lines] * 1)
#     with open("../data/txt/data_model.csv", "w") as out_file:
#         with open("../data/txt/link_keywords.txt", "r") as keywords_file:
#             keywords_stripped = (line.strip() for line in keywords_file)
#             keywords_lines = (line for line in keywords_stripped if line)
#             keywords_grouped = zip(*[keywords_lines] * 1)
#
#             writer = csv.writer(out_file)
#             writer.writerow(["url", "keywords"])
#             for url, keyword in zip(grouped, keywords_grouped):
#                 writer.writerow([url, keyword])
