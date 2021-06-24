import os
import tarfile
from urllib.request import urlretrieve


def fetch_housing_data(housing_url: str, housing_path: str) -> None:
    """Fetch data from an url and store them locally."""
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
