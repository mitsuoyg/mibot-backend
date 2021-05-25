import firebase_admin
from firebase_admin import credentials, storage as storageFirebase

class FlaskFirebase:
    
    def init_app(self, app):
        cred = credentials.Certificate('./credentials.json')
        firebase_admin.initialize_app(cred, {
            'storageBucket': app.config['STORAGE_BUCKET']
            })
        self.bucket = storageFirebase.bucket()
    def getBucket(self):
        return self.bucket
