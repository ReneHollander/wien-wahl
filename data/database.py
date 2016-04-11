from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from util import read_fully


class WienWahlDatabase:
    def __init__(self, connectionstring='sqlite+pysqlite:///wienwahl.db', create=False):
        self.engine = create_engine(connectionstring)

        self.conn = self.engine.connect()
        self.rawconn = self.engine.raw_connection()

        if create:
            self.rawconn.executescript(read_fully('sql/create.sql'))

        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        self.Election = self.Base.classes.election
        self.Constituency = self.Base.classes.constituency
        self.District = self.Base.classes.district
        self.JudicalDistrict = self.Base.classes.judicaldistrict
        self.Party = self.Base.classes.party
        self.Candidacy = self.Base.classes.candidacy
        self.Votes = self.Base.classes.votes
        self.session = Session(self.engine)


db = WienWahlDatabase(create=True)
