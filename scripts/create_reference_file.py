import json
import fire
import dvc.api

def create_path_from_md5(md5, levels=1, leveldepth=2, prefix="s3://mesoscaleclassifications/files/md5/"):
    """
    >>> create_path_from_md5('99914b932bd37a50b983c5e7c90ae93b')
    'files/md5/99/914b932bd37a50b983c5e7c90ae93b'
    >>> create_path_from_md5('99914b932bd37a50b983c5e7c90ae93b', levels=2)
    'files/md5/99/91/4b932bd37a50b983c5e7c90ae93b'
    >>> create_path_from_md5('99914b932bd37a50b983c5e7c90ae93b', leveldepth=5)
    'files/md5/99914/b932bd37a50b983c5e7c90ae93b'
    """
    path = prefix
    for i in range(levels):
        path += md5[i*leveldepth:(i+1)*leveldepth] + "/"
    path += md5[levels*leveldepth:]
    return path

def create_reference_dict(data):
    result = {item["relpath"]: [create_path_from_md5(item["md5"])] for item in data}
    reference_dict = {"version":1, "refs":result}
    return reference_dict

def create_reference_file(data, filename="reference.json"):
    with open(filename, 'w') as fp:
        json.dump(data, fp)

def load_dvc_dir_file(filename):
    with open(filename, 'r') as fp:
        md5_lookup = json.load(fp)
        return md5_lookup

def get_dir_file(filename):
    url = dvc.api.get_url(filename)
    cache_path = "/".join(url.split("/")[-2:])
    return ".dvc/cache/files/md5/" + cache_path

def main(filename, reference_file="reference.json"):
    dvc_dir_file = get_dir_file(filename)
    md5_lookup = load_dvc_dir_file(dvc_dir_file)
    reference_dict = create_reference_dict(md5_lookup)
    create_reference_file(reference_dict, reference_file)

if __name__=='__main__':
    fire.Fire(main)