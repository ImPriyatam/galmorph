import sys
import os

# Add the path to the galmorph package (adjust as needed)
sys.path.append(os.path.abspath("../galmorph"))

# Now try importing something from core
from galmorph.core import GalMorph # Replace with actual function

# Call the function to see if it works
result = GalMorph("data/morphologies_snapshot_data.pkl")  # Add required arguments
print(result)
