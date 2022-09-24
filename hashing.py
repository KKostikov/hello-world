import hashlib
import os


BUF_SIZE = 1024*1024  # lets read stuff in chunks!
top='D:\\Downloads\\'
files_dict={}

for root, dirs, files in os.walk(top):
    for name in files:
        cur_path=os.path.join(root, name)
        with open(cur_path, 'rb') as f:
            sha1 = hashlib.sha1()
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        files_dict[cur_path]=sha1.hexdigest()


print(f"Processed {len(files_dict)} files")

duplicates={}
uniqs={}
for k,v in files_dict.items():
    if v in uniqs.values():
        duplicates[k]=v
    else:
        uniqs[k]=v
print(f"Duplicates list:\n {duplicates.keys()}")