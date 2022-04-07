import json
import psycopg2
from flask import Flask
from flask import request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import jsonify
import os
from datetime import date


app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

class RegisterWebsite(Base):
    """Register Website frpm model which has all details -table names & columns"""
    __tablename__ = 'e_commerce_website'
    __table_args__ = {'schema':'register'}
    firstName =  Column("first_name",String)
    secondName = Column('second_name',String)
    age = Column('age',Integer)
    emailId = Column('email_id',String)
    mobileNumuber = Column('mobile_num',String, primary_key=True)
    password = Column('password',String)
    confirmPassword  = Column('confirm_password',String)

@app.route('/getAllRecords', methods = ['GET'])
def getRegisterRecords():
    result = session.query(RegisterWebsite.firstName,RegisterWebsite.secondName).all()
    print(type(result))
    return str(result)




@app.route('/getSingleRecords', methods = ['GET'])
def getRegisterSingleRecords():
    request_mobile_num = request.args.get('phone')
    result = session.query(RegisterWebsite).\
       filter(RegisterWebsite.mobileNumuber==request_mobile_num).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)

@app.route('/getSelectedAllRecords', methods = ['GET'])
def getRegisterSelectedRecords():
    # myStr = "34344343434,9866366177".split(",") # ['34344343434','9866366177']
    request_mobile_num = [int(numbers) for numbers in request.args.get('mobile').split(",")]
    result = session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber.\
                                                  in_(request_mobile_num)).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)


app.run(debug=False)




