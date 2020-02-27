import json
import re




with open("generated_phrases.json",'r') as infile:
    with open("fixed_generated_phrases.json",'w') as outfile:
        data = json.load(infile)

        fixed_dict = {}

        for k,v in data.items():
            first_paragraphs = v.split("\n")[0:]
            last_paragraph = v.split("\n")[-1:]
            if last_paragraph[-1] != ".":
                sentence = str(last_paragraph[0])
                fragment_removed = re.split(r'(?<=\.) ', sentence)[0:-1]
                new_v = first_paragraphs + fragment_removed
            fixed_dict[k] = new_v
        print(fixed_dict)

        json.dump(fixed_dict, outfile)

