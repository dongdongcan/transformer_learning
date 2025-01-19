# Copyright (c) 2024 dongdongcan
# This code is licensed under the MIT License.
# See the LICENSE file for details.


from gensim.models import KeyedVectors

# load the google word2vec model
filename = "GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(filename, binary=True)

# calculate: (king - man) + woman = ?
src = "king"
src_attr = "man"
dst_attr = "women"

result = model.most_similar(positive=[src, dst_attr], negative=[src_attr], topn=1)
print(src + " + " + dst_attr + " - " + src_attr + " = ")
print(result)

src = "China"
src_attr = "country"
dst_attr = "capital"

result = model.most_similar(positive=[src, dst_attr], negative=[src_attr], topn=1)
print(src + " + " + dst_attr + " - " + src_attr + " = ")
print(result)
