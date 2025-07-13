from ckipnlp.pipeline import CkipPipeline, CkipDocument

pipeline = CkipPipeline()
doc = CkipDocument(raw='中文字耶，啊哈哈哈')

# Word Segmentation
pipeline.get_ws(doc)
print(doc.ws)
for line in doc.ws:
    print(line.to_text())