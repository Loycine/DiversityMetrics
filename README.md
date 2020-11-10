# DiversityMetrics
This  is the implementation of self-CIDEr and LSA-based diversity metrics (only for python 2.7). If you think this is helpful for your work, please cite the paper: [Qingzhong Wang and Antoni Chan. Describing like humans: on diversity in image captioning. CVPR, 2019](http://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Describing_Like_Humans_On_Diversity_in_Image_Captioning_CVPR_2019_paper.html)

## Note ##
To compute the CIDEr score, TF-IDF file is required. Now, the TF-IDF is obtained from textcaps training dataset. And to compute the diversity, multiple captions for each image should be generated and the format must be the same as the file ./results/merge_results.json.

## Evaluation ##
### prepare
```
conda env export > div-metric.yaml
```

### run
1. Generating multiple captions for each image, for example 10 for each.
2. Put the json file in ./results and make sure that the format is the same as that of merge_results.json.
3. python diversity_evalscripts.py
