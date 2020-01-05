from exts import db


# Survey table
class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name
        
#Obsevation table
class Observation(db.Model):
    __tablename__ = 'observation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    value = db.Column(db.Float)
    frequency = db.Column(db.Integer)


