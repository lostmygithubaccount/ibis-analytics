# imports
import ibis
import dagster

from dag import functions as f


# assets
@dagster.asset
def extract_docs():
    """
    Load the docs data.
    """
    docs = f.clean_data(ibis.read_csv("data/ingest/docs/*.csv*"))
    return docs
