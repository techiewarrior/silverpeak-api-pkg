# Read all yaml files in specified directory
#
def readYAML(path):
    for entry in os.listdir(path):
        if entry.endswith('.yml'):
          with open(entry, 'r') as file:
              dict = yaml.load(file, Loader=yaml.FullLoader)
#
# place hostname into "name" and "tag, to be used in API post later
          name = (dict['applianceInfo']['hostname'])
          tag = (dict['applianceInfo']['hostname'])
          file.close()
#
# open and read yaml file as text into a string, so it can be converted to base64 encoding
          f = open(entry, "r")
          text = f.read()
#
# convert the string obatained from the yaml file to base64 encoding
          conversion = base64.b64encode(text.encode("utf-8"))
#
# decode base64 from bytes to string, to get rid of the "b' 'characters"
          data = conversion.decode()

          return(name, tag, data)

#end
