import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("packagedata-af408-firebase-adminsdk-yck30-c2d21e09a6.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

def add_to_db(id,l,b,h,dw,shape,volume):
    db.collection('Packages').add({
                                'ID':id,
                                'length':l,
                                'breadth':b,
                                'height':h,
                                'dead weight': dw,
                                'shape':shape,
                                'volume':volume
                                })


