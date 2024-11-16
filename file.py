import pydicom as dicom
import matplotlib.pyplot as plt
path = "./img/1.2.392.200036.9125.4.0.537867047.1085172.2889392510.dcm"
ds=dicom.dcmread(path,force=True)
#print(x)
ds.file_meta.TransferSyntaxUID = dicom.uid.ImplicitVRLittleEndian  # or whatever is the correct transfer syntax for the file
plt.imshow(ds.pixel_array,cmap=plt.cm.gray)
plt.show()
