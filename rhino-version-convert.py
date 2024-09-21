import rhino3dm
model_filename = input("Model to be converted: ")
model = rhino3dm.File3dm.Read(model_filename)
vers=input("Rhino version for converting to: ")

model.Write(str(vers)+model_filename, int(vers))
print('Converted')
