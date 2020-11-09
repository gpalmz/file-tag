from tag_match import eval_str
from tag import Tag

tag_query_0 = '(or (= hi "bye") (= name "grant"))'
tag_query_1 = '(and (= hi "bye") (= name "grant"))'
tag_query_2 = '(and (= city "boston") (not (= name "grant")) (or (= hi 2) (= hi 3)))'
tag_query_3 = '(< num-bytes 10)'
tag_query_4 = '(has hi)'
tag_query_5 = '(= name nickname)'
tag_query_6 = '(< num-users size num-bytes)'
tag_query_7 = '(has hi city)'

tags_0 = [
    Tag('ho', 'bye'),
    Tag('hi', 'bye'),
]
tags_1 = [
    Tag('ho', 'bye'),
    Tag('hi', 'bye'),
    Tag('name', 'grant'),
]
tags_2 = [
    Tag('hi', 2),
    Tag('city', 'boston'),
    Tag('name', 'gary'),
]
tags_3 = [
    Tag('hi', 2),
    Tag('city', 'boston'),
    Tag('name', 'grant'),
]
tags_4 = [
    Tag('hi', 3),
    Tag('city', 'boston'),
    Tag('name', 'gary'),
]
tags_5 = [
    Tag('hi', 2),
    Tag('city', 'ny'),
    Tag('name', 'gary'),
]
tags_6 = [
    Tag('num-bytes', 6),
]
tags_7 = [
    Tag('num-bytes', 26),
]
tags_8 = [
    Tag('hi', None),
]
tags_9 = [
    Tag('name', 'grant'),
    Tag('nickname', 'grant'),
]
tags_10 = [
    Tag('name', 'grant'),
    Tag('nickname', 'garth'),
]
tags_11 = [
    Tag('num-users', 5),
    Tag('size', 1000),
    Tag('num-bytes', 10000),
]
tags_12 = [
    Tag('num-users', 5),
    Tag('size', 100000),
    Tag('num-bytes', 10000),
]

assert eval_str(tag_query_0, tags_0)
assert not eval_str(tag_query_1, tags_0)
assert eval_str(tag_query_1, tags_1)
assert eval_str(tag_query_2, tags_2)
assert not eval_str(tag_query_2, tags_3)
assert eval_str(tag_query_2, tags_4)
assert not eval_str(tag_query_2, tags_5)
assert eval_str(tag_query_3, tags_6)
assert not eval_str(tag_query_3, tags_7)
assert eval_str(tag_query_4, tags_8)
assert not eval_str(tag_query_4, tags_7)
assert eval_str(tag_query_4, tags_5)
assert not eval_str(tag_query_0, tags_8)
assert eval_str(tag_query_5, tags_9)
assert not eval_str(tag_query_4, tags_10)
assert eval_str(tag_query_6, tags_11)
assert not eval_str(tag_query_6, tags_12)
assert eval_str(tag_query_7, tags_2)
assert not eval_str(tag_query_7, tags_0)
