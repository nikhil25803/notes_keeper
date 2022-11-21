from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'])


class Hash():

    def bcrypt(password:str):
        return pwd_cxt.hash(password)

    def verify(password, hashed_password):
        return pwd_cxt.verify(password, hashed_password)