from configparser import ConfigParser


def parse_config_file(file_name):
    config = ConfigParser()
    config.read(file_name)
    sections = {}
    for section in config.sections():
        sections[section] = dict(config.items(section))
    return sections


def create_config_file(file_name, sections):
    config = ConfigParser()
    for section, options in sections.items():
        del sections[section]['env']
        config[section] = options
    with open(file_name, 'w') as file:
        config.write(file)


def split_data(_data, environment):
    return {section: options for section, options in _data.items() if options.get('env') == environment}


if __name__ == '__main__':
    data = parse_config_file('mess.ini')
    prod_sections = split_data(data, 'prod')
    create_config_file('prod_config.ini', prod_sections)
    dev_sections = split_data(data, 'dev')
    create_config_file('dev_config.ini', dev_sections)
