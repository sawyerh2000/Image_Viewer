#import PIL.Image as Image
import io
import sql
import pip
import importlib

def runtime_installer(package):
    try:
        return importlib.import_module(package) 
    except:
        pip.main(["install", package])
    return importlib.import_module(package)

#method to convert image to bytes:
def getBytes(path):
    with open (path, 'rb') as file: #open image as read binary
        blob = file.read() #read binary of file and save it to blob
    return blob #return blob


#method to display image (takes byte tuple from database as arg):
def showImage(byte_tuple): #bytes argument should be sql.getInfo() call
    bytes=io.BytesIO(byte_tuple[0][1]) #readable bytemap for image from tupple in list
    img=PIL.Image.open(bytes) #create Image object using bytes
    img.show() #display image

if __name__ == '__main__':
    PIL = runtime_installer('PIL')
#driver loop - gets user input for choice 
while True:
    choice = input("\n1) Get image\n2) Add image\n3) Get File names\n4) Quit\n")
    if choice=='1':
        name = input("What is the name of the blob? ")
        try:
            showImage(sql.getInfo(name))
        except:
            print("Invalid name, try again.")
    elif choice=='2':
        name = input("What would you like the blob to be named? ")
        path = input("What is the file path? (use \\\) ")
        try:
            sql.addInfo(name, getBytes(path))
        except:
            print("Invalid name or path, try again.")
    elif choice=='3':
        sql.getFilenames()
    elif choice=='4':
        break
    else:
        print("Enter valid option (1-4).")



    


