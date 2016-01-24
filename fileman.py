import os
class Fileman(object) :
    def __init__(self):
        self.extensions = self.get_extensions()
        self.folder = self.get_folder_location()
    def get_extensions(self):
		#extensions list and theirs folder, make sure the folder is already exists if not, the create new one
        self.extensions = {}
        self.extensions['Music'] = ['mp3', 'flac', 'wav', 'ogg', 'aac'] # mp3, flac, wav files should moved to Music folder
        self.extensions['Pictures'] = ['jpg', 'jpeg', 'png']
        self.extensions['Video'] = ['mkv', 'avi', 'mpeg', 'mp4', '3gp', 'flv']
        self.extensions['Documents'] = ['doc', 'docx', 'pdf', 'xls', 'xlsx', 'csv']
        self.extensions['Compressed'] = ['rar', 'zip', 'gz', '7zip']
        self.extensions[os.path.join('Pictures', 'gif')] = ['gif']
        self.extensions['Programs'] = ['exe', 'msi']
        self.extensions['scripts'] = ['php', 'js', 'html', 'sql', 'htm', 'css', 'json', 'py', 'pyw']
        return self.extensions
    def get_folder_location(self):
        folder_location = r'C:\Users\ANdersoN\Downloads'; #change this to your download folder or some folder you want to manage
        return folder_location
    def read_directory(self):
        return os.listdir(self.get_folder_location()) #read folder's contents
    def get_file_extension(self, filename):
        extension = os.path.splitext(filename)[1] #het the file extension of a file, why? coz i need to match the file's ext with available exts to get it's folder
        return extension
    def get_folder_name(self, filename):
        the_folder = None
        for j, (key, value) in enumerate(self.extensions.items()):
			#here i match the file extension with all available extension o get the file destination folder when moving IT
           if self.get_file_extension(filename).lower().replace('.','') in value: 
               the_folder = key
        return the_folder
        
    def move_it(self, source, destination):
        if (os.path.isfile(source) == False): #does the source file is exists?
            return 'File not found'
        elif (os.path.isdir(os.path.dirname(destination)) == False): #does the destination folder is exists?
            return 'Directory no found'
        else:
            if (os.path.isfile(destination)): #does the destination folder contain a file with the same name with the source file?
                os.remove(destination) # if yes, delete it
                os.rename(source, destination) #here i start to move the file
                return 'Success w/ overwritting'
            else:
                try:
                   os.rename(source, destination) 
                   return 'Success w/o overwritting'
                except Exception as inst:
                    return 'Failed : '+ inst

        
            
