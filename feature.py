import yaml

class Feature:
    def __init__(self):
			with open('features.yaml', 'r') as config_file:
				self.features = yaml.load(config_file)

    def is_enabled(self, feature_name):
        return self.features[feature_name]
