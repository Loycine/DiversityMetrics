import json

with open("annotations/textcaptions_val.json",'r') as load_f:
    load_dict = json.load(load_f)

    for key in load_dict:
        print(key)

    
    dump_dict = []
    image_caption = {}
    for caption in load_dict['annotations']:
        image_id = caption['image_id']
        one_caption  = caption['caption']
        if image_id not in image_caption:
            image_caption[image_id] = []
            image_caption[image_id].append(one_caption)
        else:
            image_caption[image_id].append(one_caption)

    for key in image_caption:
        dump_dict.append({'image_id':key, 'captions':image_caption[key]})
    
    print(dump_dict[0:5])

with open("results/merge_results.json","w") as dump_f:
    json.dump(dump_dict,dump_f)