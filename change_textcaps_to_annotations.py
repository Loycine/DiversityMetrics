import json

if __name__ == "__main__":
    target = {'info': 'textcaps', 'images':[], 'license':'textcaps', 'annotations':[]}
    annotations = target['annotations']


    with open('annotations/textcaps.json') as f:
        textcaps = json.load(f)

    for x in textcaps[1:]:
        annotation = {'image_id': x['image_id'], 'id': x['caption_id'], 'caption': x['caption_str']}
        annotations.append(annotation)
        
    
    with open('annotations/textcaptions_val.json', 'w') as f:
        json.dump(target, f)