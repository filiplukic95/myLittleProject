import sqlalchemy
import sqlalchemy.orm as orm
import os
import configparser

class NoSettingsFileError(Exception):
    def __init__(self):
        super().__init__("Settings File is not set. Set value of SETTINGS_FILE constant.")

class MandatorySectionError(Exception):
    def __init__(self, section_name : str):
        super().__init__(f"""Section "{section_name}" is mandatory and must be defined in INI file.""")

class MandatoryFieldError(Exception):
    def __init__(self, field_name : str):
        super().__init__(f"""Field "{field_name}" is mandatory and must be defined in INI file.""")


class DBURLString:

    @staticmethod
    def make(path : str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        config = configparser.ConfigParser()
        with open(path, "r") as f:
            config.read_file(f) 
        if not config.has_section("database"):
            raise MandatorySectionError("database")
        db_section = dict(config.items("database"))
        madatory_fields = ["db_protocol", "db_lib", "host", "db_name"]
        for field in madatory_fields:
            if not field in db_section.keys():
                raise MandatoryFieldError(field)

        url = db_section["db_protocol"] + "+" + db_section["db_lib"] + "://"
        if "user" in db_section.keys():
            url += db_section["user"]
            if "password" in db_section.keys():
                url += ":" + db_section["password"]
            url += "@"
        url += db_section["host"]
        if "port" in db_section.keys():
            url += ":" + db_section["port"]
        url += "/" + db_section["db_name"] + "?charset=utf8"
        return url 


class DBEngine:
    SETTINGS_FILE = ""
    ENGINE = None 

    def __init__(self):
        if DBEngine.SETTINGS_FILE == "":
            raise NoSettingsFileError() 
        self.engine = sqlalchemy.create_engine(DBURLString.make(DBEngine.SETTINGS_FILE), echo=True)

    @staticmethod
    def connect() -> sqlalchemy.Connection:
        if DBEngine.ENGINE is None:
            DBEngine.ENGINE = DBEngine()
        return DBEngine.ENGINE.engine.connect()

class DBMetaData:
    INSTANCE = None 

    @staticmethod
    def get() -> sqlalchemy.MetaData:
        if DBMetaData.INSTANCE is None:
            DBMetaData.INSTANCE = sqlalchemy.MetaData()
        return DBMetaData.INSTANCE

class DBManager:
    BASE = None
    SESSION = None

    @staticmethod
    def get_base() -> orm.DeclarativeMeta:
        if DBManager.BASE is None:
            DBManager.BASE = orm.declarative_base()
        return DBManager.BASE

    @staticmethod
    def session() -> orm.Session:
        if (DBManager.SESSION is None) or \
           (DBManager.SESSION is not None and not DBManager.SESSION.is_active):
           DBManager.SESSION = orm.Session(DBEngine.connect())
        return DBManager.SESSION