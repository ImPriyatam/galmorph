import astropy as ap
def print_attrs(name, obj):
    print(name)
    for key, val in obj.attrs.items():
        print("    %s: %s" % (key, val))
import h5py
f = h5py.File("morphologies_deeplearn.hdf5",'r')
# f.visititems(print_attrs) #this will print all keys and values associated with the file
print(f['Snapshot_25']['P_Disk'][:])
print(len(f['Snapshot_25']['P_Disk'][:]))