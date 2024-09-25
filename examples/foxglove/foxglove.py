from cyclonedds.idl._support import Endianness
from foxglove import Outer

# Create an empty Outer sample and serialize it
sample = Outer(inners=[])
data = sample.serialize(endianness=Endianness.Little, use_version_2=True)

# Print the CDR serialized data
print(list(data))
