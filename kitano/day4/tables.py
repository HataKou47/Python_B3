import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Holiday(Base):
     # データベース内のテーブル名を指定します。
    __tablename__ = 'holiday'
    # 祝日の日付を格納するカラムで、主キーとして設定されています。
    holi_date = Column('holi_date', Date, primary_key = True)
    # 祝日の名前を格納するカラムです。
    holi_text = Column('holi_text', String(20))

#テーブル：Attendnumの定義
# Attendnumクラスは、来場者数を管理するためのテーブルの構造を定義します。
class Attendnum(Base):
     # データベース内のテーブル名を指定します。
    __tablename__ = 'attendnum'
    # 来場日を格納するカラムで、主キーの一部として設定されています。
    date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)    
    child = Column('child', Integer) 

def main(args):
    """
    メイン関数
    """
     # 定義したテーブル構造に基づいて、データベースにテーブルを作成します。
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        # スクリプトが直接実行された場合に、メイン関数を呼び出します。
        main(sys.argv)