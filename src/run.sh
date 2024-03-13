# These two lines gives you an empty train.jsonl to start with
# please comment these two lines later
rm train.jsonl
touch train.jsonl

cp train.jsonl tmp.jsonl

# option s gives extra ouput. option v is verbose.
python -m pytest -s -v generate_json.py
python -m pytest -s -v call_pgai.py
# pytest generate_json.py
# pytest call_pgai.py

cp tmp.jsonl train.jsonl
