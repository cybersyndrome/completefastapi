from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@127.0.0.1:3306/todoapp"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@database-2.c1imifssjm3c.us-east-1.rds.amazonaws.com:5432/todoapp"
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:password@database-1.c1imifssjm3c.us-east-1.rds.amazonaws.com:3306/todoapp" 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# acts as a registry of information about a certain set of classes that descend from that base 
# its not common to have more than one base