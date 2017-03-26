import csv

with open("../data/txt/relevant_video_links.txt", "r") as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = zip(*[lines] * 1)
    with open("../data/txt/data_model.csv", "w") as out_file:
        with open("../data/txt/link_keywords.txt", "r") as keywords_file:
            keywords_stripped = (line.strip() for line in keywords_file)
            keywords_lines = (line for line in keywords_stripped if line)
            keywords_grouped = zip(*[keywords_lines] * 1)

            writer = csv.writer(out_file)
            writer.writerow(["url", "keywords"])
            for url, keyword in zip(grouped, keywords_grouped):
                writer.writerow([url, keyword])
