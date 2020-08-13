# Read specified yaml file.
# Find the appliance name in the file, and place into the "name" and "tag" variables.
# Take YAML configuration info and convert to base64 encoding.
# Return "name", "tag", and "data" from function.

def readYAML(filename):
    import base64
    import yaml

    with open(filename, 'r') as file:
        dict = yaml.load(file, Loader=yaml.FullLoader)

# place hostname into "name" and "tag"

        name = (dict['applianceInfo']['hostname'])
        tag = (dict['applianceInfo']['hostname'])
        file.close()

# open and read yaml file as text into a string, so it can be converted to base64 encoding

        f = open(filename, "r")
        text = f.read()

# convert the string obatained from the yaml file to base64 encoding


        conversion = base64.b64encode(text.encode("utf-8"))

# decode base64 from bytes to string, to get rid of the " 'b' characters"

        data = conversion.decode()

        return name, tag, data

### For local testing ###

if __name__ == '__main__':

    print('\n ****************************************************************')
    print('\n    This module was ran directly. It is for testing only.')
    print('    It will read all .yml files within the specified directory')
    print('    No configurations will be uploaded to Orchestrator.')
    print('    This section can serve as an example for looping over many')
    print('    .yml files, in a \'main\' type function.')
    print('\n **************************************************************** \n')

    def readTEST(path):
        import os
        import base64
        import yaml

        for entry in os.listdir(path):
            if entry.endswith('.yml'):
                filename = os.path.join(path, entry)
                with open(filename, 'r') as file:
                    dict = yaml.load(file, Loader=yaml.FullLoader)

                # place hostname into "name" and "tag", to be used in API post later

                name = (dict['applianceInfo']['hostname'])
                tag = (dict['applianceInfo']['hostname'])
                file.close()

                # open and read yaml file as text into a string, so it can be converted to base64 encoding

                f = open(filename, "r")
                text = f.read()

                # convert the string obatained from the yaml file to base64 encoding

                conversion = base64.b64encode(text.encode("utf-8"))

                # decode base64 from bytes to string, to get rid of the " 'b' characters"

                data = conversion.decode()

                print('name: ' + name + ',' + ' tag: ' + tag + ' data: ' + data)


    path = r'C:\Users\janderson.JANDERSON-W10\Box Sync\Jason Anderson\Sync\GitHub\lab-ecv-autoDeployment\lab-ecv-autoDeployment'
    readTEST(path)

#end
