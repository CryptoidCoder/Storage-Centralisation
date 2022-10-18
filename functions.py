# module imports
import os
import requests

from dotenv import load_dotenv
load_dotenv()

# Dictionary of storage locations
storagelocations = os.getenv("storagelocations")

# Dictionary of cloud locations
cloudlocations= os.getenv("cloudlocations")

# Upload to drive (account, directory/file, location)
# Up-load to Mega (account, directory/file, location)

# compress (.7z/.tar.gz/.zip)

