from datetime import datetime
from opinions_app import db


class Opinion(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  text = db.Column(db.Text, nullable=False)
  source = db.Column(db.String(256))
  added_by = db.Column(db.String(64))
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def to_dict(self):
    return dict(
        id=self.id,
        title=self.title,
        text=self.text,
        source=self.source,
        added_by=self.added_by,
        timestamp=self.timestamp,
    )

  def from_dict(self, data):
    for field in ['title', 'text', 'source', 'added_by']:
      if field in data:
        setattr(self, field, data[field])