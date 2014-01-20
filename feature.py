class Feature:
    def __init__(self, app):
    	self.app = app

    def is_enabled(self, feature_name):
        return self.app.config['features'][feature_name]
