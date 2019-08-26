import os
import yaml


def scan_spec_file(spec_file):
    '''
    read contents of yaml specifications file.  return a dictionary.
    '''
    spec_file = os.path.expanduser(spec_file)
    if not os.path.isfile(spec_file):
        #log.error("spec_file not found: {}".format(spec_file))
        print("spec_file not found: {}".format(spec_file))
        return None
    #log.debug("loading spec file: {}".format(spec_file))
    with open(spec_file) as f:
        try:
            spec = yaml.safe_load(f.read())
        except (yaml.scanner.ScannerError, UnicodeDecodeError):
            #log.error("{} not a valid yaml file".format(spec_file))
            print("{} not a valid yaml file".format(spec_file))
            return None
        except Exception as e:
            #log.error("cant load spec_file '{}': {}".format(spec_file, e))
            print("cant load spec_file '{}': {}".format(spec_file, e))
            return None
    #log.debug("spec: {}".format(config))
    return spec
